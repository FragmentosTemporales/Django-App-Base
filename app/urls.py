from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from app.schema import schema
from productos.schemas import schema_producto
from empresa.schemas import schema_empresa
from . import views
from mensajes.views import create_mensaje, get_mensajes_by_empresa

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('mensajes/crear/', create_mensaje, name='create_mensaje'),
    path('mensajes/empresa/<int:empresa_id>/', get_mensajes_by_empresa, name='get_mensajes_by_empresa'),
]
