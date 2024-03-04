from django.urls import path

from . import views

urlpatterns = [
    path('conversation_view/<int:robot_id>/<str:robot_role>',views.conversation_view,name='conversation_view'),
    path('create_robot/', views.create_robot, name='create_robot'),
    path('get_studentRobots_by_id/<int:student_id>',views.get_student_robots_by_id,name='getStudentRobotsById'),
    path('get_teacherRobots_by_id/<int:teacher_id>', views.get_teacher_robots_by_id, name='getTeacherRobotsById'),
    path('get_messages_by_robot_id/<int:robot_id>',views.get_messages_by_robot_id,name='getMessagesByRobotId'),
]