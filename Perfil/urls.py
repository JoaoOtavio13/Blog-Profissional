from django.urls import path
from Perfil.views import *

urlpatterns=[
    path('',index, name='home')
]