from django.http import JsonResponse
from .utils import verify_admin_token
import logging

logger = logging.getLogger(__name__)

class AdminAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # 不需要验证token的路径
        self.exempt_paths = [
            '/api/admin/login',
        ]

    def __call__(self, request):
        # 记录请求路径
        logger.debug(f"AdminAuthMiddleware: 处理请求 {request.path}")
        
        # 只处理/api/admin/开头的请求
        if not request.path.startswith('/api/admin/'):
            logger.debug(f"AdminAuthMiddleware: 不处理非管理员路径 {request.path}")
            return self.get_response(request)
            
        # 检查请求路径是否在豁免列表中
        if request.path in self.exempt_paths:
            logger.debug(f"AdminAuthMiddleware: 豁免路径 {request.path}")
            return self.get_response(request)

        logger.debug(f"AdminAuthMiddleware: 需要验证token的路径 {request.path}")
        
        # 验证token
        token = request.headers.get('Authorization')
        if not token:
            logger.debug("AdminAuthMiddleware: 未提供token")
            return JsonResponse({
                'code': 401,
                'message': '未提供管理员token',
                'data': ''
            })
        
        admin_id, is_super = verify_admin_token(token)
        if not admin_id:
            logger.debug("AdminAuthMiddleware: token无效或已过期")
            return JsonResponse({
                'code': 401,
                'message': '管理员token无效或已过期',
                'data': ''
            })
        
        logger.debug(f"AdminAuthMiddleware: token验证成功，admin_id={admin_id}, is_super={is_super}")
        request.admin_id = admin_id
        request.is_super_admin = is_super
        return self.get_response(request) 