from django.db import models
from django.utils import timezone


class BaseModelo(models.Model):
    creado = models.DateTimeField(default=(timezone.now() - timezone.timedelta(hours=3)))

    class Meta:
        abstract = True


class Categoria(BaseModelo):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(BaseModelo):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return super().__str__()
