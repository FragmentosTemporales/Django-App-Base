import graphene
from .empresa_query import Query
from .empresa_mutation import Mutation


schema_empresa= graphene.Schema(query=Query, mutation=Mutation)
