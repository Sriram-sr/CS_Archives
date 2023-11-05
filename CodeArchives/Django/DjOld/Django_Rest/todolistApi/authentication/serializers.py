from pyexpat import model
from unittest.util import _MAX_LENGTH, _MIN_COMMON_LEN
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100,min_length=6,write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
