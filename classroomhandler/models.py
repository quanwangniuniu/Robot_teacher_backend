from django.db import models
from studenthandler.models import StudentUser
from teacherhandler.models import TeacherUser


class RobotClassRoom(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=255,unique=True)
    class_avatar = models.CharField(max_length=100,default='duck')
    teacher = models.ManyToManyField(TeacherUser, related_name='classrooms', blank=True)
    student = models.ManyToManyField(StudentUser, related_name='classrooms', blank=True)

    def __str__(self):
        return self.class_name


class ClassRoomMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    class_id = models.IntegerField()
    message_content = models.CharField(max_length=2000)
    user_name = models.CharField(max_length=100,default='li')
    user_type = models.CharField(max_length=20)
    message_avatar = models.CharField(max_length=50)