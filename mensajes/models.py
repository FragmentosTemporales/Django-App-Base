from django.db import models
from app.models import BaseModel
from empresa.models import Empresa


class Mensaje(BaseModel):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    mensaje = models.TextField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='mensajes')

    def __str__(self):
        return super().__str__()

    @classmethod
    def get_mensajes_by_empresa(cls, empresa_id):
        return cls.objects.filter(empresa__id=empresa_id)