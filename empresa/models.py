from django.db import models
from app.models import BaseModel


class Empresa(BaseModel):
    nombre = models.CharField(max_length=255)
    run = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
