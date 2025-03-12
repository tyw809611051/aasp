from django.urls import path
from .views import (
    hello_world, 
    register, 
    login, 
    upload_attachment,
    get_keypoints,
    get_au_recognition,
    get_au_intensity,
    get_depression_detection,
    get_anxiety_detection,
    get_emotion_detection,
    get_attention_detection,
    get_pain_detection,
    get_personality_detection
)

urlpatterns = [
    path('hello/', hello_world, name='hello-world'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('upload', upload_attachment, name='upload-attachment'),
    path('keypoints', get_keypoints, name='get-keypoints'),
    path('au-recognition', get_au_recognition, name='get-au-recognition'),
    path('au-intensity', get_au_intensity, name='get-au-intensity'),
    path('depression', get_depression_detection, name='get-depression-detection'),
    path('anxiety', get_anxiety_detection, name='get-anxiety-detection'),
    path('emotion', get_emotion_detection, name='get-emotion-detection'),
    path('attention', get_attention_detection, name='get-attention-detection'),
    path('pain', get_pain_detection, name='get-pain-detection'),
    path('personality', get_personality_detection, name='get-personality-detection'),
] 