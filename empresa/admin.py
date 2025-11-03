from django.contrib import admin
from .models import Empresa


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'run', 'direccion', 'website', 'creado')
    search_fields = ('nombre', 'run')
    exclude = ('creado',)

admin.site.register(Empresa, EmpresaAdmin)