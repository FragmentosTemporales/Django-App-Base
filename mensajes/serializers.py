from rest_framework import serializers
from .models import Mensaje
from empresa.models import Empresa


class MensajeSerializer(serializers.ModelSerializer):
    """Serializer for Mensaje model with validation and nested empresa details."""

    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        source='empresa',
        write_only=True
    )
    empresa = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Mensaje
        fields = ['id', 'nombre', 'apellido', 'correo', 'telefono', 'mensaje', 'empresa_id', 'empresa', 'creado']
        read_only_fields = ['id', 'creado']

    def get_empresa(self, obj):
        """Return empresa details in read operations"""
        return {
            'id': obj.empresa.id,
            'nombre': obj.empresa.nombre
        }

    def validate_correo(self, value):
        """Validate email format"""
        if '@' not in value or '.' not in value.split('@')[-1]:
            raise serializers.ValidationError("Email inválido")
        return value

    def validate(self, data):
        """Validate that required fields are present"""
        if not data.get('empresa'):
            raise serializers.ValidationError({"empresa_id": "Este campo es requerido"})
        return data
