from django.urls import path
from . import views

urlpatterns = [
    path('admin_login/', views.adminLogin, name='adminLogin'),
    path('get_all_students/',views.getAllStudents,name='getAllStudents'),
    path('get_all_teachers/', views.getAllTeachers, name='getAllTeachers'),
    path('get_all_robots/',views.getAllRobots,name='getAllRobots'),
    path('get_all_class/',views.getAllClasses,name='getAllClass'),
    path('edit_student/<int:student_id>',views.edit_student_by_id,name='editStudent'),
    path('add_student/',views.add_student,name='addStudent'),
    path('edit_teacher/<int:teacher_id>',views.edit_teacher_by_id,name='editTeacher'),
    path('edit_robot/<int:conversation_id>',views.edit_robot_by_id,name='editRobot'),
    path('edit_class/<int:class_id>', views.edit_classroom_by_id, name='editClass'),
    path('add_teacher/',views.add_teacher,name='addTeacher'),
    path('add_class/',views.add_class,name='addClass'),

    # 添加其他URL配置
]