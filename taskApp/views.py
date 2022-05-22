from pipes import Template
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from taskApp.models import UserType, Task
from .serializers import RegisterSerializer, TaskSerailizer, UserTypeSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

from taskApp import serializers


class RegisterAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, validated_data):
        register = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        register.save()
        return register


class UserTypeApiView(ListCreateAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer()

    def create(self, validated_data):
        print("0000000000000000000000000")
        register = UserType.objects.create(
            user=validated_data["user"],
            user_type=validated_data["user_type"]

        )
        register.save()
        return register


class TaskListApiView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerailizer

    def create(self, validated_data):
        task = User.objects.create(
            title=validated_data["title"],
            task_date=validated_data["task_date"],
            status=validated_data["status"],
            description=validated_data['description']
        )
        task.save()
        return task


# def post(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.save()
