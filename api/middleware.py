from django.http import JsonResponse
from .utils import verify_token
import logging

logger = logging.getLogger(__name__)

class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # 不需要验证token的路径
        self.exempt_paths = [
            '/api/register',
            '/api/login',
            '/api/hello/',
            '/media/'  # 添加media路径豁免
        ]

    def __call__(self, request):
        # 记录请求路径
        logger.debug(f"TokenAuthMiddleware: 处理请求 {request.path}")
        
        # 不处理管理员路径
        if request.path.startswith('/api/admin/'):
            logger.debug(f"TokenAuthMiddleware: 不处理管理员路径 {request.path}")
            return self.get_response(request)
            
        # 检查请求路径是否以豁免路径开头
        if any(request.path.startswith(path) for path in self.exempt_paths):
            logger.debug(f"TokenAuthMiddleware: 豁免路径 {request.path}")
            return self.get_response(request)

        logger.debug(f"TokenAuthMiddleware: 需要验证token的路径 {request.path}")
        
        # 验证token
        token = request.headers.get('Authorization')
        if not token:
            logger.debug("TokenAuthMiddleware: 未提供token")
            return JsonResponse({
                'code': 401,
                'message': '未提供token',
                'data': ''
            })
        
        user_id = verify_token(token)
        if not user_id:
            logger.debug("TokenAuthMiddleware: token无效或已过期")
            return JsonResponse({
                'code': 401,
                'message': 'token无效或已过期',
                'data': ''
            })
        
        logger.debug(f"TokenAuthMiddleware: token验证成功，user_id={user_id}")
        request.user_id = user_id
        return self.get_response(request) 