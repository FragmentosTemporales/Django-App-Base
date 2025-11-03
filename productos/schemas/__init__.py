import graphene
from .producto_query import Query
from .producto_mutation import Mutation


schema_producto = graphene.Schema(query=Query, mutation=Mutation)
