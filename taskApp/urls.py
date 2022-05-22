from django.urls import path
from taskApp import views

app_name = "userapp"
urlpatterns = [
    path('api/register/', views.RegisterAPIView.as_view(), name='register'),
    path('api/user/', views.UserTypeApiView.as_view(), name='user'),
    path('api/task/', views.TaskListApiView.as_view(), name='task'),

]
