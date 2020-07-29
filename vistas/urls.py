from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include

from .views import vistaClass, vistaConf, nextClas, hora_list, hora_create
from Login.views import LoginClass, l

urlpatterns = [
    
    path('',LoginClass.as_view(), name='login'),
    path('accounts/login/',LoginClass.as_view(), name='login'),
    path('logout/',l.as_view() ,name ='logout'),
    path('index/', login_required(vistaClass.as_view()), name='index' ),
    path('next/',login_required(nextClas.as_view()), name='next'),
    path('configure/',login_required(vistaConf.as_view()), name='configure' ),
    path('lista/',login_required(hora_list), name='hora_list' ),
    url(r'^agregar',login_required(hora_create), name='hora_create'),
]
 