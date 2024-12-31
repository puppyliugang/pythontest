from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    nickname = db.Column(db.String(64))
    avatar = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    status = db.Column(db.SmallInteger, default=1)  # 1: 正常, 0: 禁用
    language = db.Column(db.String(10), default='zh')  # 添加语言字段
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'phone': self.phone,
            'nickname': self.nickname,
            'avatar': self.avatar,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'status': self.status,
            'language': self.language
        }

class LoginLog(db.Model):
    __tablename__ = 'login_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(64))
    user_agent = db.Column(db.String(256))
    login_type = db.Column(db.String(20))  # password, qrcode
    status = db.Column(db.Boolean, default=True)  # True: 成功, False: 失败 
    language = db.Column(db.String(10), default='zh')  # 添加语言字段