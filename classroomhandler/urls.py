# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('teacher_classrooms/<int:teacher_id>/',views.get_teacher_classrooms,name='get_teacher_classrooms'),
    path('create_class/', views.create_class, name='create_class'),
    path('edit_class/<int:class_id>/', views.edit_class, name='edit_class'),
]
