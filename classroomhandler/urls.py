# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('teacher_classrooms/<int:teacher_id>/',views.get_teacher_classrooms,name='get_teacher_classrooms'),
    path('student_classrooms/<int:student_id>/', views.get_student_classrooms, name='get_student_classrooms'),
    path('student_participate/',views.student_participate_class,name='student_participate_class'),
    path('teacher_participate/', views.teacher_participate_class, name='teacher_participate_class'),
    path('create_class/', views.create_class, name='create_class'),
    path('edit_class/<int:class_id>/', views.edit_class, name='edit_class'),
    path('get_users_in_classrooms/<int:class_id>/', views.get_users_in_classrooms, name='get_student_classrooms'),
    path('get_classroom_name_byId/<int:class_id>/',views.get_classroom_name_byId,name='get_classroom_name_byId'),
    path('get_classroom_messages/<int:class_id>',views.get_classroom_messages,name='get_classroom_messages'),
    path('send_messages/<int:class_id>/<str:username>',views.sendMessage,name='send_messages'),
]
