from rest_framework import serializers
from .models import RobotClassRoom,ClassRoomMessage

class RobotClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotClassRoom
        fields = '__all__'

class ClassRoomMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoomMessage
        fields = '__all__'