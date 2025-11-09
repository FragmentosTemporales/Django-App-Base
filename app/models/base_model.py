from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    creado = models.DateTimeField(default=(timezone.now() - timezone.timedelta(hours=3)))

    class Meta:
        abstract = True
