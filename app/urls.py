from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from productos.schemas import schema_producto

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('productos/', include('productos.urls')),
    path("graphql_productos/", GraphQLView.as_view(graphiql=True, schema=schema_producto))
]
