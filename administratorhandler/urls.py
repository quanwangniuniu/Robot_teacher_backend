from django.urls import path
from . import views

urlpatterns = [
    path('admin_login/', views.adminLogin, name='adminLogin'),
    # 添加其他URL配置
]