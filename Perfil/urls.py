from django.urls import path
from Perfil.views import *

urlpatterns = [
    path('', index, name='home'),
    path('hobbies/', hobbies, name='hobbies'),
    path('instituicao/', instituicao, name='instituicao'),
]