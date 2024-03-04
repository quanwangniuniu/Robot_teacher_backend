from rest_framework import serializers
from .models import RobotClassRoom

class RobotClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotClassRoom
        fields = '__all__'