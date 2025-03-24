from django.db import models

# Create your models here.

class AaspUser(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name='用户名')
    email = models.CharField(max_length=128, unique=True, verbose_name='邮箱')
    password = models.CharField(max_length=128, verbose_name='密码')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'aasp_user'
        verbose_name = '用户表'

class AaspUserAttachment(models.Model):
    ATTACHMENT_TYPE_IMAGE = 1
    ATTACHMENT_TYPE_VIDEO = 2
    
    ATTACHMENT_TYPE_CHOICES = (
        (ATTACHMENT_TYPE_IMAGE, '图片'),
        (ATTACHMENT_TYPE_VIDEO, '视频'),
    )
    
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_type = models.SmallIntegerField(
        choices=ATTACHMENT_TYPE_CHOICES,
        default=ATTACHMENT_TYPE_IMAGE,
        verbose_name='附件类型'
    )
    attachment_url = models.CharField(max_length=255, default='', verbose_name='附件地址')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_user_attachment'
        verbose_name = '用户上传附件表'

class AaspKeypointDetection(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_id = models.IntegerField(default=0, verbose_name='附件ID')
    keyword = models.CharField(max_length=128, default='', verbose_name='关键词')
    value = models.CharField(max_length=64, default='', verbose_name='值')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_keypoint_detection'
        verbose_name = '人脸关键点检测表'

class AaspAuRecognition(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_id = models.IntegerField(default=0, verbose_name='附件ID')
    keyword = models.CharField(max_length=128, default='', verbose_name='关键词')
    value = models.CharField(max_length=64, default='', verbose_name='值')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_au_recognition'
        verbose_name = '人脸AU识别'

class AaspAuIntensityDetection(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_id = models.IntegerField(default=0, verbose_name='附件ID')
    keyword = models.CharField(max_length=128, default='', verbose_name='关键词')
    value = models.CharField(max_length=64, default='', verbose_name='值')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_au_intensity_detection'
        verbose_name = '人脸AU强度检测'

class AaspDepressionDetection(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_id = models.IntegerField(default=0, verbose_name='附件ID')
    value = models.CharField(max_length=64, default='', verbose_name='值')
    desc = models.CharField(max_length=512, default='', verbose_name='描述')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_depression_detection'
        verbose_name = '抑郁症检测'

class AaspAnxietyDetection(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_id = models.IntegerField(default=0, verbose_name='附件ID')
    value = models.CharField(max_length=64, default='', verbose_name='值')
    desc = models.CharField(max_length=512, default='', verbose_name='描述')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_anxiety_detection'
        verbose_name = '焦虑检测'

class AaspEmotionDetection(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_id = models.IntegerField(default=0, verbose_name='附件ID')
    value = models.CharField(max_length=64, default='', verbose_name='情绪值')
    desc = models.CharField(max_length=512, default='', verbose_name='描述')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_emotion_detection'
        verbose_name = '人脸情绪检测'

class AaspAttentionDetection(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_id = models.IntegerField(default=0, verbose_name='附件ID')
    value = models.CharField(max_length=64, default='', verbose_name='情绪值')
    desc = models.CharField(max_length=512, default='', verbose_name='描述')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_attention_detection'
        verbose_name = '注意力检测'

class AaspPainDetection(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_id = models.IntegerField(default=0, verbose_name='附件ID')
    value = models.CharField(max_length=64, default='', verbose_name='值')
    desc = models.CharField(max_length=512, default='', verbose_name='描述')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_pain_detection'
        verbose_name = '疼痛检测'

class AaspPersonalityDetection(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='用户ID')
    attachment_id = models.IntegerField(default=0, verbose_name='附件ID')
    keyword = models.CharField(max_length=128, default='', verbose_name='关键词')
    value = models.CharField(max_length=64, default='', verbose_name='值')
    desc = models.CharField(max_length=512, default='', verbose_name='描述')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aasp_personality_detection'
        verbose_name = '性格检测'

class AaspAdmin(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name='管理员用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    is_super = models.BooleanField(default=False, verbose_name='是否超级管理员')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'aasp_admin'
        verbose_name = '管理员表'
