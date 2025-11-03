from graphene_django import DjangoObjectType
from empresa.models import Empresa


class EmpresaType(DjangoObjectType):
    class Meta:
        model = Empresa
        fields = "__all__"