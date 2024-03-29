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

class MeicyModel(models.Model):
    model_id = models.AutoField(primary_key = True)
    learningRate = models.FloatField(default=0.0213)
    batchSize = models.IntegerField(default=64)
    epoches = models.IntegerField(default=85)
    hiddenLayerSize = models.IntegerField(default=256)
    vocabularySize = models.BigIntegerField(default=100000)
    maxSeqLength = models.IntegerField(default=500)
    dropoutRate = models.FloatField(default=0.32)
    gradientClippingThreshold = models.FloatField(default=3.26)
    optimizer = models.CharField(max_length=100,default="adam")
    lossFunction = models.CharField(max_length=100,default="meanSquaredError")