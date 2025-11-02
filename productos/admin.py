from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado')
    search_fields = ('nombre',)
    exclude = ('creado',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock','puntaje', 'categoria', 'creado')
    search_fields = ('nombre',)
    exclude = ('creado',)



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)