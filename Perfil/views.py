from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    lista_usuario=Usuario.objects.all()
    context={
        'usuario':lista_usuario
    }
    return render(request, 'Perfil/index.html',context)

def instituicao(request):
    lista_instituicao=Instituicao.objects.all()
    context={
        'instituicao': lista_instituicao
    }
    return render(request, 'Perfil/instituicao.html',context)

def hobbies(request):
    return render(request,'Perfil/hobbies.html')