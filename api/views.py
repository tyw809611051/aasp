from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AaspUser, AaspUserAttachment, AaspKeypointDetection, AaspAuRecognition, AaspAuIntensityDetection, AaspDepressionDetection, AaspAnxietyDetection, AaspEmotionDetection, AaspAttentionDetection, AaspPainDetection, AaspPersonalityDetection
from .utils import (
    generate_password_hash, 
    generate_token, 
    success_response, 
    error_response
)
from django.db import IntegrityError
import os
from django.conf import settings
from datetime import datetime

# Create your views here.

@api_view(['GET'])
def hello_world(request):
    return success_response("Hello, World!")

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    # 参数验证
    if not all([username, email, password]):
        return error_response('所有字段都是必填的')
    
    try:
        # 创建用户
        user = AaspUser.objects.create(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        return success_response('注册成功')
    except IntegrityError:
        return error_response('用户名或邮箱已存在')

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    # 参数验证
    if not all([username, password]):
        return error_response('用户名和密码都是必填的')
    
    try:
        user = AaspUser.objects.get(
            username=username,
            password=generate_password_hash(password)
        )
        token, expire_in = generate_token(user.id)
        return success_response('登录成功', {
            'token': token,
            'expire_in': expire_in
        })
    except AaspUser.DoesNotExist:
        return error_response('用户名或密码错误', 401)

@api_view(['POST'])
def upload_attachment(request):
    # 检查是否有文件
    if 'file' not in request.FILES:
        return error_response('请选择要上传的文件')
    
    file = request.FILES['file']
    content_type = file.content_type
    
    # 判断文件类型
    if content_type in settings.ALLOWED_IMAGE_TYPES:
        attachment_type = AaspUserAttachment.ATTACHMENT_TYPE_IMAGE
    elif content_type in settings.ALLOWED_VIDEO_TYPES:
        attachment_type = AaspUserAttachment.ATTACHMENT_TYPE_VIDEO
    else:
        return error_response('只能上传图片或视频文件')
    
    # 生成文件保存路径
    file_ext = os.path.splitext(file.name)[1]
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{request.user_id}{file_ext}"
    relative_path = os.path.join('attachments', filename)
    file_path = os.path.join(settings.MEDIA_ROOT, 'attachments', filename)
    
    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 保存文件
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    
    # 保存记录到数据库
    attachment = AaspUserAttachment.objects.create(
        user_id=request.user_id,
        attachment_type=attachment_type,
        attachment_url=os.path.join(settings.MEDIA_URL, relative_path)
    )
    
    return success_response('上传成功', {
        'type': attachment_type,
        'url': attachment.attachment_url
    })

@api_view(['GET'])
def get_keypoints(request):
    attachment_id = request.GET.get('attachment_id')
    
    # 参数验证
    if not attachment_id:
        return error_response('附件ID不能为空')
    
    try:
        attachment_id = int(attachment_id)
    except ValueError:
        return error_response('附件ID必须是数字')
    
    # 查询数据
    keypoints = AaspKeypointDetection.objects.filter(
        user_id=request.user_id,
        attachment_id=attachment_id
    ).values('keyword', 'value')
    
    # 转换为列表
    keypoint_list = list(keypoints)
    
    return success_response('获取成功', keypoint_list)

@api_view(['GET'])
def get_au_recognition(request):
    attachment_id = request.GET.get('attachment_id')
    
    # 参数验证
    if not attachment_id:
        return error_response('附件ID不能为空')
    
    try:
        attachment_id = int(attachment_id)
    except ValueError:
        return error_response('附件ID必须是数字')
    
    # 查询数据
    au_list = AaspAuRecognition.objects.filter(
        user_id=request.user_id,
        attachment_id=attachment_id
    ).values('keyword', 'value')
    
    return success_response('获取成功', list(au_list))

@api_view(['GET'])
def get_au_intensity(request):
    attachment_id = request.GET.get('attachment_id')
    
    # 参数验证
    if not attachment_id:
        return error_response('附件ID不能为空')
    
    try:
        attachment_id = int(attachment_id)
    except ValueError:
        return error_response('附件ID必须是数字')
    
    # 查询数据
    intensity_list = AaspAuIntensityDetection.objects.filter(
        user_id=request.user_id,
        attachment_id=attachment_id
    ).values('keyword', 'value')
    
    return success_response('获取成功', list(intensity_list))

@api_view(['GET'])
def get_depression_detection(request):
    attachment_id = request.GET.get('attachment_id')
    
    # 参数验证
    if not attachment_id:
        return error_response('附件ID不能为空')
    
    try:
        attachment_id = int(attachment_id)
    except ValueError:
        return error_response('附件ID必须是数字')
    
    # 查询数据
    try:
        detection = AaspDepressionDetection.objects.filter(
            user_id=request.user_id,
            attachment_id=attachment_id
        ).values('value', 'desc').first()
        
        if not detection:
            return error_response('未找到相关数据')
            
        return success_response('获取成功', detection)
    except Exception as e:
        return error_response('获取数据失败')

@api_view(['GET'])
def get_anxiety_detection(request):
    attachment_id = request.GET.get('attachment_id')
    
    # 参数验证
    if not attachment_id:
        return error_response('附件ID不能为空')
    
    try:
        attachment_id = int(attachment_id)
    except ValueError:
        return error_response('附件ID必须是数字')
    
    # 查询数据
    try:
        detection = AaspAnxietyDetection.objects.filter(
            user_id=request.user_id,
            attachment_id=attachment_id
        ).values('value', 'desc').first()
        
        if not detection:
            return error_response('未找到相关数据')
            
        return success_response('获取成功', detection)
    except Exception as e:
        return error_response('获取数据失败')

@api_view(['GET'])
def get_emotion_detection(request):
    attachment_id = request.GET.get('attachment_id')
    
    # 参数验证
    if not attachment_id:
        return error_response('附件ID不能为空')
    
    try:
        attachment_id = int(attachment_id)
    except ValueError:
        return error_response('附件ID必须是数字')
    
    # 查询数据
    try:
        detection = AaspEmotionDetection.objects.filter(
            user_id=request.user_id,
            attachment_id=attachment_id
        ).values('value', 'desc').first()
        
        if not detection:
            return error_response('未找到相关数据')
            
        return success_response('获取成功', detection)
    except Exception as e:
        return error_response('获取数据失败')

@api_view(['GET'])
def get_attention_detection(request):
    attachment_id = request.GET.get('attachment_id')
    
    # 参数验证
    if not attachment_id:
        return error_response('附件ID不能为空')
    
    try:
        attachment_id = int(attachment_id)
    except ValueError:
        return error_response('附件ID必须是数字')
    
    # 查询数据
    try:
        detection = AaspAttentionDetection.objects.filter(
            user_id=request.user_id,
            attachment_id=attachment_id
        ).values('value', 'desc').first()
        
        if not detection:
            return error_response('未找到相关数据')
            
        return success_response('获取成功', detection)
    except Exception as e:
        return error_response('获取数据失败')

@api_view(['GET'])
def get_pain_detection(request):
    attachment_id = request.GET.get('attachment_id')
    
    # 参数验证
    if not attachment_id:
        return error_response('附件ID不能为空')
    
    try:
        attachment_id = int(attachment_id)
    except ValueError:
        return error_response('附件ID必须是数字')
    
    # 查询数据
    try:
        detection = AaspPainDetection.objects.filter(
            user_id=request.user_id,
            attachment_id=attachment_id
        ).values('value', 'desc').first()
        
        if not detection:
            return error_response('未找到相关数据')
            
        return success_response('获取成功', detection)
    except Exception as e:
        return error_response('获取数据失败')

@api_view(['GET'])
def get_personality_detection(request):
    attachment_id = request.GET.get('attachment_id')
    
    # 参数验证
    if not attachment_id:
        return error_response('附件ID不能为空')
    
    try:
        attachment_id = int(attachment_id)
    except ValueError:
        return error_response('附件ID必须是数字')
    
    # 查询数据
    try:
        personality_list = AaspPersonalityDetection.objects.filter(
            user_id=request.user_id,
            attachment_id=attachment_id
        ).values('keyword', 'value', 'desc')  # 注意这里增加了desc字段
        
        if not personality_list:
            return error_response('未找到相关数据')
            
        return success_response('获取成功', list(personality_list))
    except Exception as e:
        return error_response('获取数据失败')
