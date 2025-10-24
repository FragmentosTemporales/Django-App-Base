from django.db import models

# Create your models here.

class BaseModelo(models.Model):
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Categoria(BaseModelo):
    nombre = models.CharField(max_length=255)


class Producto(BaseModelo):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre