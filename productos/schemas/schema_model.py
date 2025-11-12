from graphene_django import DjangoObjectType
from productos.models import Producto, Categoria, EmpresaCategoriaProducto


class ProductoType(DjangoObjectType):
    class Meta:
        model = Producto
        fields = "__all__"


class CategoriaType(DjangoObjectType):
    class Meta:
        model = Categoria
        fields = "__all__"


class EmpresaCategoriaProductoType(DjangoObjectType):
    class Meta:
        model = EmpresaCategoriaProducto
        fields = "__all__"
