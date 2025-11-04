import graphene
from empresa.models import Empresa
from empresa.schemas.schema_model import EmpresaType


class BaseEmpresa:

    @staticmethod
    def validate_run(run):
        lower_run = str(run.lower())
        if '-' not in lower_run:
            raise Exception("El RUN debe contener un guion (-)")
        # Aquí puedes agregar la lógica para validar el RUN
        elif len(lower_run) < 9:
            raise Exception("El RUN es demasiado corto.")
        elif len(lower_run) > 20:
            raise Exception("El RUN es demasiado largo.")
        return True

    @staticmethod
    def validate_nombre(nombre):
        if len(nombre) < 3:
            raise Exception("El nombre debe tener al menos 3 caracteres.")
        elif len(nombre) > 255:
            raise Exception("El nombre es demasiado largo.")
        return True


class CreateEmpresa(graphene.Mutation, BaseEmpresa):
    class Arguments:
        nombre = graphene.String(required=True)
        run = graphene.String(required=True)
        direccion = graphene.String(required=True)
        website = graphene.String()

    empresa = graphene.Field(EmpresaType)

    def mutate(self, info, nombre, run, direccion, website):
        try:

            CreateEmpresa.validate_run(run)
            CreateEmpresa.validate_nombre(nombre)

            empresa = Empresa(
                nombre=nombre,
                run=run,
                direccion=direccion,
                website=website
            )
            empresa.save()

            return CreateEmpresa(empresa=empresa)
        except Exception as e:
            raise Exception(f"Error al crear la empresa: {str(e)}")


class DeleteEmpresa(graphene.Mutation, BaseEmpresa):

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


class UpdateEmpresa(graphene.Mutation, BaseEmpresa):

    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String(required=True)
        run = graphene.String(required=True)
        direccion = graphene.String(required=True)
        website = graphene.String()

    empresa = graphene.Field(EmpresaType)

    def mutate(self, info, id, nombre, run, direccion, website):

        try:
            UpdateEmpresa.validate_nombre(nombre)
            UpdateEmpresa.validate_run(run)

            empresa = Empresa.objects.get(pk=id)
            empresa.nombre = nombre
            empresa.save()

            return UpdateEmpresa(empresa=empresa)
        except Exception as e:  
            raise Exception(f"Error al actualizar la empresa: {str(e)}")


class Mutation(graphene.ObjectType):
    create_empresa = CreateEmpresa.Field()
    delete_empresa = DeleteEmpresa.Field()
    update_empresa = UpdateEmpresa.Field()
