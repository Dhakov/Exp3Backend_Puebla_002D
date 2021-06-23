from django.db import models

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
