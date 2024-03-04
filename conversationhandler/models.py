from django.db import models

# 对话框表
class Conversation(models.Model):
    conversation_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=100,default='student')
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    title = models.CharField(max_length=100,unique=True)
    status = models.BooleanField(default=1) # 1代表正常使用 # 2 代表不启用
    robot_model = models.CharField(max_length=100,default='qwen-max')
    robot_prompt =models.CharField(max_length=300,default='programing teacher')
    roles = models.CharField(max_length=200,default='programing teacher')

# 对话具体信息表
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    conversation_id = models.IntegerField()
    message_content = models.CharField(max_length=2000)
    message_type = models.CharField(max_length=20)
