from flask import Flask, jsonify, request, session, send_file, render_template
import redis
import qrcode
import base64
import io
import uuid
from datetime import datetime
import logging
import traceback
from captcha.image import ImageCaptcha
import random
import string
import os
from config import (FLASK_CONFIG, REDIS_CONFIG, QRCODE_CONFIG, 
                   CAPTCHA_CONFIG, TEST_ACCOUNT, LOG_CONFIG, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS)
from models import db, User, LoginLog

# 配置日志
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建文件处理器
file_handler = logging.FileHandler(LOG_CONFIG['FILENAME'], encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建格式器
formatter = logging.Formatter(LOG_CONFIG['FORMAT'])
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加处理器到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 记录应用启动信息
logger.info("Application starting...")

app = Flask(__name__)
app.config.update(FLASK_CONFIG)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

# 初始化 Redis 客户端
try:
    redis_client = redis.Redis(**REDIS_CONFIG)
    redis_client.ping()
    logger.info("Redis connection successful")
except redis.ConnectionError as e:
    logger.error(f"Redis connection failed: {e}")
    logger.error(traceback.format_exc())
    raise

# 初始化验证码生成器
image_captcha = ImageCaptcha(width=CAPTCHA_CONFIG['WIDTH'], 
                           height=CAPTCHA_CONFIG['HEIGHT'])

# 初始化数据库
db.init_app(app)

# 创建数据库表
with app.app_context():
    db.create_all()
    
    # 创建测试用户（如果不存在）
    if not User.query.filter_by(phone=TEST_ACCOUNT['PHONE']).first():
        test_user = User(phone=TEST_ACCOUNT['PHONE'])
        test_user.set_password(TEST_ACCOUNT['PASSWORD'])
        test_user.nickname = '测试用户'
        db.session.add(test_user)
        db.session.commit()

@app.route('/')
def index():
    try:
        logger.info("Rendering login page")
        return render_template('login.html')
    except Exception as e:
        logger.error(f"Error rendering login page: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/api/captcha')
def get_captcha():
    try:
        logger.info("Generating new captcha")
        # 生成随机的验证码 ID
        captcha_id = str(uuid.uuid4())
        
        # 生成随机验证码
        captcha_text = ''.join(random.choices(
            string.ascii_uppercase + string.digits, 
            k=CAPTCHA_CONFIG['LENGTH']
        ))
        
        logger.debug(f"Generated captcha text: {captcha_text}")
        
        # 将验证码存入 Redis
        redis_client.setex(
            f'captcha:{captcha_id}',
            CAPTCHA_CONFIG['EXPIRE_TIME'],
            captcha_text
        )
        
        # 将验证码 ID 存入 session
        session['captcha_id'] = captcha_id
        logger.debug(f"Stored captcha_id in session: {captcha_id}")
        
        # 生成验证码图片
        image = image_captcha.generate(captcha_text)
        logger.info("Captcha generated successfully")
        
        return send_file(
            io.BytesIO(image.read()),
            mimetype='image/png'
        )
    except Exception as e:
        logger.error(f"Captcha generation failed: {e}")
        logger.error(traceback.format_exc())
        return jsonify({'error': 'Failed to generate captcha'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        phone = data.get('phone')
        password = data.get('password')
        
        # 验证验证码
        captcha_id = session.get('captcha_id')
        if not captcha_id:
            return jsonify({
                'success': False,
                'message': 'invalid_captcha'
            })
        
        stored_captcha = redis_client.get(f'captcha:{captcha_id}')
        if not stored_captcha or stored_captcha.decode().lower() != data.get('verificationCode', '').lower():
            return jsonify({
                'success': False,
                'message': 'invalid_captcha'
            })
            
        # 查找用户
        user = User.query.filter_by(phone=phone).first()
        if user and user.check_password(password):
            # 记录登录日志
            log = LoginLog(
                user_id=user.id,
                ip_address=request.remote_addr,
                user_agent=request.user_agent.string,
                login_type='password',
                status=True
            )
            db.session.add(log)
            
            # 更新最后登录时间
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            # 设置session
            session['user_id'] = user.id
            if data.get('remember'):
                session.permanent = True
                
            return jsonify({
                'success': True,
                'message': 'login_success',
                'user': user.to_dict()
            })
            
        return jsonify({
            'success': False,
            'message': 'invalid_credentials'
        })
        
    except Exception as e:
        logger.error(f"Login failed: {e}")
        logger.error(traceback.format_exc())
        return jsonify({
            'success': False,
            'message': 'server_error'
        }), 500

@app.route('/qr-login')
def qr_login():
    return render_template('qr_login.html')

@app.route('/api/generate-qr')
def generate_qr():
    # 生成唯一的二维码ID
    qr_id = os.urandom(16).hex()
    session['qr_id'] = qr_id
    session['qr_status'] = 'pending'
    
    # 生成二维码图片
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 转换为base64
    buffered = BytesIO()
    img.save(buffered)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return jsonify({'qr_code': img_str})

@app.route('/api/check-qr-status')
def check_qr_status():
    lang = request.headers.get('Accept-Language', 'zh').split(',')[0]
    if lang not in messages:
        lang = 'zh'
    
    qr_id = session.get('qr_id')
    if not qr_id:
        return jsonify({
            'status': 'expired',
            'message': messages[lang]['qr_expired']
        })
    
    status = session.get('qr_status', 'pending')
    if status == 'scanned':
        return jsonify({
            'status': 'scanned',
            'message': messages[lang]['qr_scanned']
        })
    elif status == 'confirmed':
        return jsonify({
            'status': 'confirmed',
            'message': messages[lang]['qr_confirmed']
        })
    
    return jsonify({'status': 'pending'})

@app.errorhandler(404)
def not_found_error(error):
    logger.warning(f"404 error: {request.url}")
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {str(error)}")
    logger.error(traceback.format_exc())
    return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/qrcode/generate')
def generate_qrcode():
    try:
        logger.info("Generating QR code")
        # 生成唯一的二维码ID
        qrcode_id = str(uuid.uuid4())
        
        # 创建二维码数据
        qr_data = {
            'type': 'login',
            'id': qrcode_id,
            'timestamp': datetime.now().timestamp()
        }
        
        # 将二维码信息存入 Redis
        redis_client.setex(
            f'qrcode:{qrcode_id}',
            QRCODE_CONFIG['EXPIRE_TIME'],
            'pending'
        )
        
        # 生成二维码图片
        qr = qrcode.QRCode(
            version=QRCODE_CONFIG['VERSION'],
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=QRCODE_CONFIG['BOX_SIZE'],
            border=QRCODE_CONFIG['BORDER'],
        )
        qr.add_data(str(qr_data))
        qr.make(fit=True)
        
        # 转换为图片
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 转换为 base64
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        logger.info("QR code generated successfully")
        return jsonify({
            'success': True,
            'qrcode': qrcode_id,
            'image': f'data:image/png;base64,{img_str}'
        })
    except Exception as e:
        logger.error(f"QR code generation failed: {e}")
        logger.error(traceback.format_exc())
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/qrcode/check/<qrcode_id>')
def check_qrcode(qrcode_id):
    try:
        logger.info(f"Checking QR code status: {qrcode_id}")
        # 从 Redis 获取二维码状态
        status = redis_client.get(f'qrcode:{qrcode_id}')
        
        if status is None:
            return jsonify({
                'status': 'expired'
            })
        
        return jsonify({
            'status': status.decode() if isinstance(status, bytes) else status
        })
    except Exception as e:
        logger.error(f"QR code check failed: {e}")
        logger.error(traceback.format_exc())
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    logger.info("Starting Flask application...")
    app.run(host='0.0.0.0', port=5000, debug=True) 