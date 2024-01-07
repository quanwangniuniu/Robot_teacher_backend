from django.urls import path
from . import views

urlpatterns = [
    path('teacherRobot/', views.teacherRobot,name='teacherRobot'),
    path('teacher_login/', views.teadentLogin, name='teacherLogin'),
    # 添加其他URL配置
    path('teacher_register/',views.teacherRegister,name='teacherRegister'),
    path('get_teacherUser_by_id/<int:teacher_id>/',views.get_teacherUser_data,name='getteacherUserById'),
    path('update_teacherUser_by_id/<int:teacher_id>/',views.update_teacherUser_data,name='updateteacherUserById')
]

