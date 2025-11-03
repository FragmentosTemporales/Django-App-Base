from graphene_django import DjangoObjectType
from productos.models import Producto, Categoria


class ProductoType(DjangoObjectType):
    class Meta:
        model = Producto
        fields = ("id", "nombre", "puntaje", "categoria", "stock")


class CategoriaType(DjangoObjectType):
    class Meta:
        model = Categoria
        fields = ("id", "nombre")