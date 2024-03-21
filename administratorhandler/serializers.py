from rest_framework import serializers
from .models import MeicyModel

class MeicyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeicyModel
        fields = '__all__'
