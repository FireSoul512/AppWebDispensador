from django.urls import include, re_path,path 
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_view
from Register.views import RegisterClass

app_name = 'Register'

urlpatterns = [
    path('',RegisterClass.as_view(), name = 'Register'),
]