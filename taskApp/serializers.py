from rest_framework import serializers
from .models import UserType, Task
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    # user_type = serializers.CharField()
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


class TaskSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
