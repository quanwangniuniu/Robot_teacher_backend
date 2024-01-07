from django.db import models
from django.utils import timezone


class StudentUser(models.Model):
    student_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128)
    last_login_time = models.DateTimeField(max_length=30,default=timezone.now)
    in_class = models.CharField(max_length=20,default=None)

    def __str__(self):
        return self.username


