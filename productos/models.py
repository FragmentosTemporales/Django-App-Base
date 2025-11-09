from django.db import models
from app.models import BaseModel


class Categoria(BaseModel):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(BaseModel):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return super().__str__()
