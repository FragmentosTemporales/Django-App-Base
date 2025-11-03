import graphene
from productos.models import Producto, Categoria
from productos.schemas.schema_model import ProductoType, CategoriaType


class CreateProductoMutation(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        stock = graphene.Int(required=True)
        puntaje = graphene.Float(required=True)
        categoria_id = graphene.ID(required=True)

    producto = graphene.Field(ProductoType)

    def mutate(self, info, nombre, stock, puntaje, categoria_id):
        categoria = Categoria.objects.get(pk=categoria_id)
        producto = Producto(
            nombre=nombre,
            stock=stock,
            puntaje=puntaje,
            categoria=categoria
        )
        producto.save()
        return CreateProductoMutation(producto=producto)


class CreateCategoriaMutation(graphene.Mutation):
    """
    mutation {
        createCategoria(nombre:"Tecnología") {
            categoria {
            id,
            nombre
            }
        }
    }
    """

    class Arguments:
        nombre = graphene.String(required=True)

    categoria = graphene.Field(CategoriaType)

    def mutate(self, info, nombre):
        categoria = Categoria(nombre=nombre)
        categoria.save()
        return CreateCategoriaMutation(categoria=categoria)


class DeleteCategoriaMutation(graphene.Mutation):
    """
    mutation {
    deleteCategoria(id:3) {
        message
    }
    }
    """

    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        try:
            categoria = Categoria.objects.get(pk=id)
            categoria.delete()
            return DeleteCategoriaMutation(message="Categoría eliminada con éxito.")
        except Categoria.DoesNotExist:
            return DeleteCategoriaMutation(message="Categoría no encontrada.")


class DeleteProductoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        try:
            producto = Producto.objects.get(pk=id)
            producto.delete()
            return DeleteProductoMutation(message="Producto eliminado con éxito.")
        except Producto.DoesNotExist:
            return DeleteProductoMutation(message="Producto no encontrado.")


class UpdateCategoriaMutation(graphene.Mutation):
    """
    mutation {
        updateCategoria(
            id:1, 
            nombre: "Nueva Categoría") {
                categoria {
            nombre,
            id
            }
        }
    }
    """
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String(required=True)

    categoria = graphene.Field(CategoriaType)

    def mutate(self, info, id, nombre):
        categoria = Categoria.objects.get(pk=id)
        categoria.nombre = nombre
        categoria.save()
        return UpdateCategoriaMutation(categoria=categoria)


class UpdateProductoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String()
        stock = graphene.Int()
        puntaje = graphene.Float()

    producto = graphene.Field(ProductoType)

    def mutate(self, info, id, nombre=None, stock=None, puntaje=None, categoria_id=None):
        producto = Producto.objects.get(pk=id)
        if nombre is not None:
            producto.nombre = nombre
        if stock is not None:
            producto.stock = stock
        if puntaje is not None:
            producto.puntaje = puntaje
        if categoria_id is not None:
            categoria = Categoria.objects.get(pk=categoria_id)
            producto.categoria = categoria
        producto.save()
        return UpdateProductoMutation(producto=producto)


class Mutation(graphene.ObjectType):
    create_producto = CreateProductoMutation.Field()
    create_categoria = CreateCategoriaMutation.Field()
    delete_categoria = DeleteCategoriaMutation.Field()
    delete_producto = DeleteProductoMutation.Field()
    update_categoria = UpdateCategoriaMutation.Field()
    update_producto = UpdateProductoMutation.Field()
