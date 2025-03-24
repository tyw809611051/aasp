import jwt
from datetime import datetime, timedelta
from django.conf import settings
import hashlib
from rest_framework.response import Response

def generate_password_hash(password):
    """生成密码哈希"""
    return hashlib.md5(password.encode()).hexdigest()

def generate_token(user_id):
    """生成JWT token"""
    expire_time = datetime.utcnow() + timedelta(days=1)  # token有效期1天
    payload = {
        'user_id': user_id,
        'exp': expire_time
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    # 计算过期时间（秒）
    expire_in = int((expire_time - datetime.utcnow()).total_seconds())
    return token, expire_in

def verify_token(token):
    """验证JWT token"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def success_response(message='success', data=''):
    """成功响应"""
    return Response({
        'code': 200,
        'message': message,
        'data': data
    })

def error_response(message='error', code=400, data=''):
    """错误响应"""
    return Response({
        'code': code,
        'message': message,
        'data': data
    })

def generate_admin_token(admin_id, is_super=False):
    """生成管理员JWT token"""
    expire_time = datetime.utcnow() + timedelta(days=1)  # token有效期1天
    payload = {
        'admin_id': admin_id,
        'is_super': is_super,
        'exp': expire_time
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    # 计算过期时间（秒）
    expire_in = int((expire_time - datetime.utcnow()).total_seconds())
    return token, expire_in

def verify_admin_token(token):
    """验证管理员JWT token"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload.get('admin_id'), payload.get('is_super', False)
    except jwt.ExpiredSignatureError:
        return None, False
    except jwt.InvalidTokenError:
        return None, False 