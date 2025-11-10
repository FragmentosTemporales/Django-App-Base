from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from productos.schemas import schema_producto
from empresa.schemas import schema_empresa
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path("graphql_productos/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema_producto))),
    path("graphql_empresa/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema_empresa))),
]
