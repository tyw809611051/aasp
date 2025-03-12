# Generated by Django 4.2.20 on 2025-03-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AaspAnxietyDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                ("attachment_id", models.IntegerField(default=0, verbose_name="附件ID")),
                (
                    "value",
                    models.CharField(default="", max_length=64, verbose_name="值"),
                ),
                (
                    "desc",
                    models.CharField(default="", max_length=512, verbose_name="描述"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "焦虑检测",
                "db_table": "aasp_anxiety_detection",
            },
        ),
        migrations.CreateModel(
            name="AaspAttentionDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                ("attachment_id", models.IntegerField(default=0, verbose_name="附件ID")),
                (
                    "value",
                    models.CharField(default="", max_length=64, verbose_name="情绪值"),
                ),
                (
                    "desc",
                    models.CharField(default="", max_length=512, verbose_name="描述"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "注意力检测",
                "db_table": "aasp_attention_detection",
            },
        ),
        migrations.CreateModel(
            name="AaspAuIntensityDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                ("attachment_id", models.IntegerField(default=0, verbose_name="附件ID")),
                (
                    "keyword",
                    models.CharField(default="", max_length=128, verbose_name="关键词"),
                ),
                (
                    "value",
                    models.CharField(default="", max_length=64, verbose_name="值"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "人脸AU强度检测",
                "db_table": "aasp_au_intensity_detection",
            },
        ),
        migrations.CreateModel(
            name="AaspAuRecognition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                ("attachment_id", models.IntegerField(default=0, verbose_name="附件ID")),
                (
                    "keyword",
                    models.CharField(default="", max_length=128, verbose_name="关键词"),
                ),
                (
                    "value",
                    models.CharField(default="", max_length=64, verbose_name="值"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "人脸AU识别",
                "db_table": "aasp_au_recognition",
            },
        ),
        migrations.CreateModel(
            name="AaspDepressionDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                ("attachment_id", models.IntegerField(default=0, verbose_name="附件ID")),
                (
                    "value",
                    models.CharField(default="", max_length=64, verbose_name="值"),
                ),
                (
                    "desc",
                    models.CharField(default="", max_length=512, verbose_name="描述"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "抑郁症检测",
                "db_table": "aasp_depression_detection",
            },
        ),
        migrations.CreateModel(
            name="AaspEmotionDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                ("attachment_id", models.IntegerField(default=0, verbose_name="附件ID")),
                (
                    "value",
                    models.CharField(default="", max_length=64, verbose_name="情绪值"),
                ),
                (
                    "desc",
                    models.CharField(default="", max_length=512, verbose_name="描述"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "人脸情绪检测",
                "db_table": "aasp_emotion_detection",
            },
        ),
        migrations.CreateModel(
            name="AaspKeypointDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                ("attachment_id", models.IntegerField(default=0, verbose_name="附件ID")),
                (
                    "keyword",
                    models.CharField(default="", max_length=128, verbose_name="关键词"),
                ),
                (
                    "value",
                    models.CharField(default="", max_length=64, verbose_name="值"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "人脸关键点检测表",
                "db_table": "aasp_keypoint_detection",
            },
        ),
        migrations.CreateModel(
            name="AaspPainDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                ("attachment_id", models.IntegerField(default=0, verbose_name="附件ID")),
                (
                    "value",
                    models.CharField(default="", max_length=64, verbose_name="值"),
                ),
                (
                    "desc",
                    models.CharField(default="", max_length=512, verbose_name="描述"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "疼痛检测",
                "db_table": "aasp_pain_detection",
            },
        ),
        migrations.CreateModel(
            name="AaspPersonalityDetection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                ("attachment_id", models.IntegerField(default=0, verbose_name="附件ID")),
                (
                    "keyword",
                    models.CharField(default="", max_length=128, verbose_name="关键词"),
                ),
                (
                    "value",
                    models.CharField(default="", max_length=64, verbose_name="值"),
                ),
                (
                    "desc",
                    models.CharField(default="", max_length=512, verbose_name="描述"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "性格检测",
                "db_table": "aasp_personality_detection",
            },
        ),
        migrations.CreateModel(
            name="AaspUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=255, unique=True, verbose_name="用户名"),
                ),
                (
                    "email",
                    models.CharField(max_length=128, unique=True, verbose_name="邮箱"),
                ),
                ("password", models.CharField(max_length=128, verbose_name="密码")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "用户表",
                "db_table": "aasp_user",
            },
        ),
        migrations.CreateModel(
            name="AaspUserAttachment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(default=0, verbose_name="用户ID")),
                (
                    "attachment_type",
                    models.SmallIntegerField(
                        choices=[(1, "图片"), (2, "视频")], default=1, verbose_name="附件类型"
                    ),
                ),
                (
                    "attachment_url",
                    models.CharField(default="", max_length=255, verbose_name="附件地址"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "用户上传附件表",
                "db_table": "aasp_user_attachment",
            },
        ),
    ]
