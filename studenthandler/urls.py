from django.urls import path
from . import views

urlpatterns = [
    path('studentRobot/', views.studentRobot,name='studentRobot'),
    path('student_login/',views.studentLogin,name='studentLogin'),
    path('student_register/',views.studentRegister,name='studentRegister'),
    path('get_studentUser_by_id/<int:student_id>/',views.get_studentUser_data,name='getStudentUserById'),
    path('update_studentUser_by_id/<int:student_id>/',views.update_studentUser_data,name='updateStudentUserById'),
    path('update_studentAvatar_by_id/<int:student_id>/', views.update_studentUser_avatar,name='updatestudentAvatarById'),
]
