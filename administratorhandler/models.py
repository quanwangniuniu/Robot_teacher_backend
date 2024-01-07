from django.db import models

class AdminUser(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128)  # 存储加密后的密码，使用Django提供的密码哈希算法

    def __str__(self):
        return self.username