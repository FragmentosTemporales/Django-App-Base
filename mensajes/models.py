from django.db import models
from app.models import BaseModel
from empresa.models import Empresa


class Mensaje(BaseModel):
    """Model to store messages related to an Empresa.

    - Fields:
      - nombre: First name of the sender
      - apellido: Last name of the sender
      - correo: Email address of the sender
      - telefono: Phone number of the sender (optional)
        - mensaje: The message content
        - empresa: ForeignKey to Empresa model

    - Methods:
      - __str__: String representation of the message
        - get_mensajes_by_empresa: Class method to retrieve messages by empresa ID
    """
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    mensaje = models.TextField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='mensajes')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.empresa}"


    @classmethod
    def get_mensajes_by_empresa(cls, empresa_id):
        return cls.objects.filter(empresa__id=empresa_id)
