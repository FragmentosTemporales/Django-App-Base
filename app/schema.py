import graphene
from empresa.schemas.empresa_query import Query as EmpresaQuery
from empresa.schemas.empresa_mutation import Mutation as EmpresaMutation
from productos.schemas.producto_query import Query as ProductoQuery
from productos.schemas.producto_mutation import Mutation as ProductoMutation


class Query(
    EmpresaQuery, 
    ProductoQuery, 
    graphene.ObjectType):
    """Schema principal de consultas que combina todos los módulos"""
    pass


class Mutation(
    EmpresaMutation, 
    ProductoMutation, 
    graphene.ObjectType):
    """Schema principal de mutaciones que combina todos los módulos"""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
