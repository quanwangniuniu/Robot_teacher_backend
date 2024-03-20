from django.urls import path
from . import views

urlpatterns = [
    path('teacherRobot/', views.teacherRobot,name='teacherRobot'),
    path('teacher_login/', views.teadentLogin, name='teacherLogin'),
    path('teacher_register/',views.teacherRegister,name='teacherRegister'),
    path('get_teacherUser_by_id/<int:teacher_id>/',views.get_teacherUser_data,name='getteacherUserById'),
    path('update_teacherUser_by_id/<int:teacher_id>/',views.update_teacherUser_data,name='updateteacherUserById'),
    path('update_teacherAvatar_by_id/<int:teacher_id>/', views.update_teacherUser_avatar, name='updateteacherAvatarById'),
    path('get_teacherRobot_by_id/<int:teacher_id>/', views.getAllRobots, name='getAllRobots'),

]

