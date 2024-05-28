from django.db import models
from django.utils import timezone

# Create your models here.
class Senai(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1500)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idade = models.IntegerField()
    data = models.DateField(default=timezone.now)
    quartos = models.CharField(max_length=50)

class Salas(models.Model):
    salas = models.CharField(max_length=50, )
    numero = models.IntegerField()
    descricao = models.TextField(max_length=255)
    equipamentos = models.CharField(max_length=50)
    corredor = models.CharField(max_length=50)