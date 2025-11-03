import graphene
from productos.models import Producto, Categoria

from productos.schemas.schema_model import ProductoType, CategoriaType


class Query(graphene.ObjectType):
    hello = graphene.String(description="A typical hello world")
    productos = graphene.List(ProductoType, description="List of all products")
    producto = graphene.Field(ProductoType, id=graphene.ID(required=True), description="Get a product by ID")
    categorias = graphene.List(CategoriaType, description="List of all categories")
    categoria = graphene.Field(CategoriaType, id=graphene.ID(required=True), description="Get a category by ID")


    def resolve_productos(self, info):
        """{
           	productos {
                id,
                nombre,
                puntaje,
                stock
                    }
            }"""
        return Producto.objects.all()


    def resolve_producto(self, info, id):
        """
        {
          producto(id:1) {
            id,
            nombre,
            puntaje,
            stock
          }
          
        }
        """
        return Producto.objects.get(pk=id)


    def resolve_categorias(self, info):
        return Categoria.objects.all()


    def resolve_categoria(self, info, id):
        return Categoria.objects.get(pk=id)


    def resolve_hello(self, info):
        return "Hello, World!"
