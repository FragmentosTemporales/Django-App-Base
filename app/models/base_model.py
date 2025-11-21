from django.db import models
from django.utils import timezone
from django.forms.models import model_to_dict

class BaseModel(models.Model):
    """Abstract base model with common fields and methods.
    - Fields:
      - creado: DateTime when the record was created
    
    - Methods:
      - to_dict: Convert model instance to dictionary
    """

    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def to_dict(self):
        """Convierte la instancia a un diccionario"""
        return model_to_dict(self)
