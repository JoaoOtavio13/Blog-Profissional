from django.db import models

# Create your models here.
class Instituicao(models.Model):
    nome=models.CharField(max_length=200)
    campos=models.CharField(max_length=200)
    curso=models.CharField(max_length=200)
    nivel=models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Instrumento(models.Model):
    nome=models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome=models.CharField(max_length=200)
    idade=models.IntegerField()
    data_nascimento=models.DateField()
    cpf=models.CharField(max_length=200)
    email=models.EmailField()
    imagem=models.ImageField(upload_to='usuario/', null=True, blank=True)
    instituicao=models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    instrumento=models.ManyToManyField(Instrumento)

    def __str__(self):
        return self.nome