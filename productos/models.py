from django.db import models
from app.models import BaseModel
from empresa.models import Empresa


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


class EmpresaCategoriaProducto(BaseModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='categoria_productos')
    categoria_producto = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='empresa_categorias')

    def __str__(self):
        return f"{self.empresa.nombre} - {self.categoria_producto.nombre}"
