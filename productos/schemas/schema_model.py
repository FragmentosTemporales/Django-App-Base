from graphene_django import DjangoObjectType
from productos.models import Producto, Categoria


class ProductoType(DjangoObjectType):
    class Meta:
        model = Producto
        fields = "__all__"


class CategoriaType(DjangoObjectType):
    class Meta:
        model = Categoria
        fields = "__all__"