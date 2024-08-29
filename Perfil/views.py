from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    lista_usuario=Usuario.objects.all()
    context={
        'usuario':lista_usuario
    }
    return render(request, 'Perfil/index.html',context)