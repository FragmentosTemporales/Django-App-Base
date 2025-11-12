import graphene
from productos.models import Producto, Categoria, EmpresaCategoriaProducto

from productos.schemas.schema_model import ProductoType, CategoriaType, EmpresaCategoriaProductoType


class Query(graphene.ObjectType):
    productos = graphene.List(ProductoType, description="List of all products")
    producto = graphene.Field(ProductoType, id=graphene.ID(required=True), description="Get a product by ID")

    categorias = graphene.List(CategoriaType, description="List of all categories")
    categoria = graphene.Field(CategoriaType, id=graphene.ID(required=True), description="Get a category by ID")

    empresa_categoria_productos = graphene.List(EmpresaCategoriaProductoType, description="List of all EmpresaCategoriaProducto")
    empresa_categoria_producto = graphene.Field(EmpresaCategoriaProductoType, id=graphene.ID(required=True), description="Get an EmpresaCategoriaProducto by ID")

    def resolve_productos(self, info):
        return Producto.objects.all()


    def resolve_producto(self, info, id):
        return Producto.objects.get(pk=id)


    def resolve_categorias(self, info):
        return Categoria.objects.all()


    def resolve_categoria(self, info, id):
        return Categoria.objects.get(pk=id)


    def resolve_empresa_categoria_productos(self, info):
        return EmpresaCategoriaProducto.objects.all()


    def resolve_empresa_categoria_producto(self, info, id):
        return EmpresaCategoriaProducto.objects.get(pk=id)
