from django.db import models
from django.utils import timezone


class BaseModelo(models.Model):
    creado = models.DateTimeField(default=(timezone.now() - timezone.timedelta(hours=3)))

    class Meta:
        abstract = True


class Empresa(BaseModelo):
    nombre = models.CharField(max_length=255)
    run = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
