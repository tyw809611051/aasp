from django.urls import path
from .admin_views import (
    admin_login,
    create_admin,
    get_user_list,
    get_user_detail,
    get_dashboard_stats,
    get_admin_user_list,
    get_admin_attachment_list
)

urlpatterns = [
    path('login', admin_login, name='admin-login'),
    path('create', create_admin, name='create-admin'),
    path('users', get_user_list, name='get-user-list'),
    path('users/<int:user_id>', get_user_detail, name='get-user-detail'),
    path('dashboard', get_dashboard_stats, name='get-dashboard-stats'),
    path('user', get_admin_user_list, name='get-admin-user-list'),
    path('attachment', get_admin_attachment_list, name='get-admin-attachment-list'),
] 