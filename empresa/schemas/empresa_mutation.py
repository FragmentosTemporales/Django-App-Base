import graphene
from empresa.models import Empresa
from empresa.schemas.schema_model import EmpresaType


class CreateEmpresa(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        run = graphene.String(required=True)
        direccion = graphene.String(required=True)
        website = graphene.String()

    empresa = graphene.Field(EmpresaType)

    def mutate(self, info, nombre, run, direccion, website):
        empresa = Empresa(
            nombre=nombre,
            run=run,
            direccion=direccion,
            website=website
        )
        empresa.save()
        return CreateEmpresa(empresa=empresa)


class DeleteEmpresa(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        try:
            empresa = Empresa.objects.get(pk=id)
            empresa.delete()
            return DeleteEmpresa(message="Empresa eliminada con éxito.")
        except Empresa.DoesNotExist:
            return DeleteEmpresa(message="Empresa no encontrada.")


class UpdateEmpresa(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String(required=True)
        run = graphene.String(required=True)
        direccion = graphene.String(required=True)
        website = graphene.String()

    empresa = graphene.Field(EmpresaType)

    def mutate(self, info, id, nombre):
        empresa = Empresa.objects.get(pk=id)
        empresa.nombre = nombre
        empresa.save()
        return UpdateEmpresa(empresa=empresa)


class Mutation(graphene.ObjectType):
    create_empresa = CreateEmpresa.Field()
    delete_empresa = DeleteEmpresa.Field()
    update_empresa = UpdateEmpresa.Field()
