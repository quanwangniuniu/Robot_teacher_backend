from rest_framework import serializers
from .models import TeacherUser

class TeacherUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherUser
        fields = '__all__'