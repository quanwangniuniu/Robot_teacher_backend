from django.db import models

class TeacherUser(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128)
    teacher_avatar = models.CharField(max_length=200,default="https://api.dicebear.com/7.x/miniavs/svg?seed=1")
    def __str__(self):
        return self.username