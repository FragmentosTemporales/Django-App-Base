from django.contrib import admin
from .models import Mensaje

# Register your models here.
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo', 'telefono', 'empresa', 'creado', 'mensaje')
    search_fields = ('nombre', 'apellido', 'correo')
    exclude = ('creado',)

admin.site.register(Mensaje, MensajeAdmin)