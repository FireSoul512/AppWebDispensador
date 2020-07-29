from django.urls import path

from .views import vistaClass, vistaConf, nextClas
from Login.views import LoginClass, l

urlpatterns = [
    path('',LoginClass.as_view(), name='login'),
    path('logout/',l.as_view() ,name ='logout'),
    path('index/', vistaClass.as_view(), name='index' ),
    path('next/',nextClas.as_view(), name='next'),
    path('configure/',vistaConf.as_view(), name='configure' ),
]
