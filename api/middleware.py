from django.http import JsonResponse
from .utils import verify_token

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
        # 检查请求路径是否以豁免路径开头
        if any(request.path.startswith(path) for path in self.exempt_paths):
            return self.get_response(request)

        # 验证token
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({
                'code': 401,
                'message': '未提供token',
                'data': ''
            })
        
        user_id = verify_token(token)
        if not user_id:
            return JsonResponse({
                'code': 401,
                'message': 'token无效或已过期',
                'data': ''
            })
        
        request.user_id = user_id
        return self.get_response(request) 