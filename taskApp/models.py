from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    USER_TYPE = (
        ('manager', 'Manager'),
        ('employee', 'Employee'),
        ('client', 'Client')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    user_type = models.CharField(
        max_length=50, choices=USER_TYPE, default='manager')


class Task(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('complete', 'Complete')
    )
    title = models.CharField(max_length=250)
    task_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=100, choices=STATUS, default='pending')
    description = models.TextField()
