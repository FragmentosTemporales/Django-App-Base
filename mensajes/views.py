from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Mensaje
from .serializers import MensajeSerializer


class MensajeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Mensaje instances.
    
    Provides standard CRUD operations:
    - list: GET /api/mensajes/
    - create: POST /api/mensajes/
    - retrieve: GET /api/mensajes/{id}/
    - update: PUT /api/mensajes/{id}/
    - partial_update: PATCH /api/mensajes/{id}/
    - destroy: DELETE /api/mensajes/{id}/
    
    Additional custom action:
    - by_empresa: GET /api/mensajes/by_empresa/{empresa_id}/
    """
    queryset = Mensaje.objects.all().select_related('empresa')
    serializer_class = MensajeSerializer
    permission_classes = [AllowAny]  # Cambiar a [IsAuthenticated] en producción

    def get_queryset(self):
        """
        Optionally filter mensajes by empresa_id query parameter
        Example: GET /api/mensajes/?empresa_id=1
        """
        queryset = super().get_queryset()
        empresa_id = self.request.query_params.get('empresa_id', None)
        if empresa_id is not None:
            queryset = queryset.filter(empresa_id=empresa_id)
        return queryset

    @action(detail=False, methods=['get'], url_path='by-empresa/(?P<empresa_id>[^/.]+)')
    def by_empresa(self, request, empresa_id=None):
        """
        Custom action to get all mensajes for a specific empresa.
        URL: GET /api/mensajes/by-empresa/{empresa_id}/
        """
        mensajes = self.get_queryset().filter(empresa_id=empresa_id)
        serializer = self.get_serializer(mensajes, many=True)
        return Response(serializer.data)
