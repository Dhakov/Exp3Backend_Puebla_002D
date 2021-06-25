from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nomCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
    descCategoria = models.CharField(max_length=200, verbose_name='Descripcion de la Categoria')

    def __str__(self):
        return (self.nomCategoria)

class Software(models.Model):
    idSoftware = models.IntegerField(primary_key=True, verbose_name='Id del Software')
    nomSoftware = models.CharField(max_length=50, verbose_name='Nombre del Software')
    descSoftware = models.CharField(max_length=300, verbose_name='Descripcion del Software')
    catSoftware = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return (self.nomSoftware)

class RequisitosMin(models.Model):
    idRequisito = models.IntegerField(primary_key=True, verbose_name='Id de los Requisitos')
    sistema = models.CharField(max_length=50, verbose_name='Sistema operativo minimo')
    procesador = models.CharField(max_length=10, verbose_name='Procesador mínimo')
    memoria = models.IntegerField(verbose_name='Ram minima')
    grafico = models.CharField(max_length=80, verbose_name='GPU Minima')
    almacenamiento = models.IntegerField(verbose_name='Almacenamiento minimo')
    idSoftware = models.ForeignKey(Software, on_delete=models.CASCADE)

