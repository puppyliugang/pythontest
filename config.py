import os
from datetime import datetime

# 基础配置
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'log')

# 确保日志目录存在
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 日志配置
LOG_CONFIG = {
    'FILENAME': os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
    'FORMAT': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'LEVEL': 'DEBUG'
}

# Flask 配置
FLASK_CONFIG = {
    'SECRET_KEY': os.urandom(24),
    'SESSION_TYPE': 'redis',
    'PERMANENT_SESSION_LIFETIME': 86400,
    'TEMPLATES_AUTO_RELOAD': True,
    'DEBUG': True
}

# Redis 配置
REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0,
    'password': '',
    'decode_responses': True
}

# 二维码配置
QRCODE_CONFIG = {
    'EXPIRE_TIME': 300,
    'VERSION': 1,
    'BOX_SIZE': 10,
    'BORDER': 4
}

# 验证码配置
CAPTCHA_CONFIG = {
    'WIDTH': 120,
    'HEIGHT': 40,
    'EXPIRE_TIME': 300,  # 5分钟过期
    'LENGTH': 4,
    'FONT_SIZE': 30
}

# 测试账号配置
TEST_ACCOUNT = {
    'PHONE': '13800138000',
    'PASSWORD': '123456'
}

# MySQL 配置
MYSQL_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',  # 替换为你的 MySQL 用户名
    'password': 'Y4yhl9t!',
    'database': 'test'
}

# SQLAlchemy 配置
SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}@"
    f"{MYSQL_CONFIG['host']}:{MYSQL_CONFIG['port']}/{MYSQL_CONFIG['database']}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False 