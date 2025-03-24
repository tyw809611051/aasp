from rest_framework.decorators import api_view
from .models import AaspAdmin, AaspUser, AaspUserAttachment
from .utils import generate_password_hash, generate_admin_token, success_response, error_response
from django.db import IntegrityError
from django.db.models import Count
from django.db import models
from rest_framework.response import Response

@api_view(['POST'])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    # 参数验证
    if not all([username, password]):
        return error_response('用户名和密码都是必填的')
    
    try:
        admin = AaspAdmin.objects.get(
            username=username,
            password=generate_password_hash(password)
        )
        token, expire_in = generate_admin_token(admin.id, admin.is_super)
        return success_response('登录成功', {
            'token': token,
            'expire_in': expire_in,
            'is_super': admin.is_super
        })
    except AaspAdmin.DoesNotExist:
        return error_response('用户名或密码错误', 401)

@api_view(['POST'])
def create_admin(request):
    # 检查是否是超级管理员
    if not request.is_super_admin:
        return error_response('只有超级管理员才能创建管理员账号', 403)
        
    username = request.data.get('username')
    password = request.data.get('password')
    is_super = request.data.get('is_super', False)
    
    # 参数验证
    if not all([username, password]):
        return error_response('用户名和密码都是必填的')
    
    try:
        # 创建管理员
        admin = AaspAdmin.objects.create(
            username=username,
            password=generate_password_hash(password),
            is_super=is_super
        )
        return success_response('创建管理员成功')
    except IntegrityError:
        return error_response('管理员用户名已存在')

@api_view(['GET'])
def get_user_list(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 10))
    
    start = (page - 1) * page_size
    end = page * page_size
    
    # 获取用户列表
    users = AaspUser.objects.all().order_by('-created_at')[start:end]
    total = AaspUser.objects.count()
    
    user_list = []
    for user in users:
        user_list.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return success_response('获取成功', {
        'list': user_list,
        'total': total,
        'page': page,
        'page_size': page_size
    })

@api_view(['GET'])
def get_user_detail(request, user_id):
    try:
        user = AaspUser.objects.get(id=user_id)
        
        # 获取用户上传的附件数量
        attachment_count = AaspUserAttachment.objects.filter(user_id=user_id).count()
        
        return success_response('获取成功', {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            'attachment_count': attachment_count
        })
    except AaspUser.DoesNotExist:
        return error_response('用户不存在')

@api_view(['GET'])
def get_dashboard_stats(request):
    # 获取用户总数
    user_count = AaspUser.objects.count()
    
    # 获取附件总数
    attachment_count = AaspUserAttachment.objects.count()
    
    # 获取图片和视频数量
    image_count = AaspUserAttachment.objects.filter(attachment_type=AaspUserAttachment.ATTACHMENT_TYPE_IMAGE).count()
    video_count = AaspUserAttachment.objects.filter(attachment_type=AaspUserAttachment.ATTACHMENT_TYPE_VIDEO).count()
    
    # 获取最近7天的用户注册数据
    from django.utils import timezone
    import datetime
    
    today = timezone.now().date()
    seven_days_ago = today - datetime.timedelta(days=6)
    
    daily_stats = []
    for i in range(7):
        day = seven_days_ago + datetime.timedelta(days=i)
        count = AaspUser.objects.filter(
            created_at__year=day.year,
            created_at__month=day.month,
            created_at__day=day.day
        ).count()
        daily_stats.append({
            'date': day.strftime('%Y-%m-%d'),
            'count': count
        })
    
    return success_response('获取成功', {
        'user_count': user_count,
        'attachment_count': attachment_count,
        'image_count': image_count,
        'video_count': video_count,
        'daily_stats': daily_stats
    })

@api_view(['GET'])
def get_admin_user_list(request):
    """获取用户列表（符合特定格式的分页数据）"""
    page = int(request.GET.get('current', 1))  # 注意这里使用current作为页码参数
    page_size = int(request.GET.get('pageSize', 10))
    
    # 可选的搜索参数
    search = request.GET.get('search', '')
    
    # 构建查询
    query = AaspUser.objects.all()
    
    # 如果有搜索条件，添加过滤
    if search:
        query = query.filter(
            models.Q(username__icontains=search) | 
            models.Q(email__icontains=search)
        )
    
    # 获取总数
    total = query.count()
    
    # 分页
    start = (page - 1) * page_size
    end = page * page_size
    users = query.order_by('-created_at')[start:end]
    
    # 构建用户列表
    user_list = []
    for user in users:
        # 获取用户上传的附件数量
        attachment_count = AaspUserAttachment.objects.filter(user_id=user.id).count()
        
        user_list.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            'attachment_count': attachment_count
        })
    
    # 返回符合要求格式的数据
    return Response({
        'code': 200,
        'message': '获取成功',
        'data': {
            'list': user_list,
            'total': total,
            'current': page,
            'pageSize': page_size,
            'success': True
        }
    })

@api_view(['GET'])
def get_admin_attachment_list(request):
    """获取用户上传附件列表（符合特定格式的分页数据）"""
    page = int(request.GET.get('current', 1))
    page_size = int(request.GET.get('pageSize', 10))
    
    # 可选的搜索和过滤参数
    search = request.GET.get('search', '')
    attachment_type = request.GET.get('type', '')  # 可以按类型过滤
    user_id = request.GET.get('user_id', '')  # 可以按用户ID过滤
    
    # 构建查询
    query = AaspUserAttachment.objects.all()  # 移除 select_related('user_id')
    
    # 应用过滤条件
    if attachment_type and attachment_type.isdigit():
        query = query.filter(attachment_type=int(attachment_type))
    
    if user_id and user_id.isdigit():
        query = query.filter(user_id=int(user_id))
    
    # 获取总数
    total = query.count()
    
    # 分页
    start = (page - 1) * page_size
    end = page * page_size
    attachments = query.order_by('-created_at')[start:end]
    
    # 构建附件列表
    attachment_list = []
    for attachment in attachments:
        # 获取用户名
        try:
            user = AaspUser.objects.get(id=attachment.user_id)
            username = user.username
        except AaspUser.DoesNotExist:
            username = f"未知用户(ID:{attachment.user_id})"
        
        # 获取附件类型名称
        attachment_type_name = dict(AaspUserAttachment.ATTACHMENT_TYPE_CHOICES).get(
            attachment.attachment_type, '未知类型'
        )
        
        attachment_list.append({
            'id': attachment.id,
            'user_id': attachment.user_id,
            'username': username,
            'attachment_type': attachment.attachment_type,
            'attachment_type_name': attachment_type_name,
            'attachment_url': attachment.attachment_url,
            'created_at': attachment.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    # 返回符合要求格式的数据
    return Response({
        'code': 200,
        'message': '获取成功',
        'data': {
            'list': attachment_list,
            'total': total,
            'current': page,
            'pageSize': page_size,
            'success': True
        }
    }) 