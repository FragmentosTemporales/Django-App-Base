import graphene
from empresa.models import Empresa
from empresa.schemas.schema_model import EmpresaType


class Query(graphene.ObjectType):
    empresas = graphene.List(EmpresaType, description="Lista de todas las empresas")
    empresa = graphene.Field(EmpresaType, id=graphene.ID(required=True), description="Empresa por ID")


    def resolve_empresas(self, info):
        return Empresa.objects.all()


    def resolve_empresa(self, info, id):
        return Empresa.objects.get(pk=id)