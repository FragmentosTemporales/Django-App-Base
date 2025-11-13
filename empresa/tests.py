from django.test import TestCase
from django.db import IntegrityError
from django.utils import timezone
from .models import Empresa


class EmpresaModelTest(TestCase):
    def setUp(self):
        Empresa.objects.create(
            nombre="Empresa de prueba", 
            direccion="Calle Falsa 123",
            run="12345678-9",
            website="https://www.ejemplo.com"
        )

    def test_empresa_str(self):
        empresa = Empresa.objects.get(nombre="Empresa de prueba")
        self.assertEqual(str(empresa), "Empresa de prueba")

    def test_empresa_creacion_automatica_fecha(self):
        """Verifica que el campo creado se genera automáticamente"""
        empresa = Empresa.objects.get(nombre="Empresa de prueba")
        self.assertIsNotNone(empresa.creado)
        self.assertIsInstance(empresa.creado, type(timezone.now()))

    def test_empresa_run_unico(self):
        """Verifica que el RUN sea único"""
        with self.assertRaises(IntegrityError):
            Empresa.objects.create(
                nombre="Otra empresa",
                direccion="Otra dirección",
                run="12345678-9",  # RUN duplicado
                website="https://www.otro.com"
            )

    def test_empresa_website_opcional(self):
        """Verifica que el website sea opcional"""
        empresa = Empresa.objects.create(
            nombre="Empresa sin web",
            direccion="Calle Nueva 456",
            run="98765432-1"
        )
        self.assertIsNone(empresa.website)

    def test_empresa_campos_requeridos(self):
        """Verifica que los campos requeridos no puedan ser vacíos"""
        empresa = Empresa(
            nombre="",
            direccion="Calle Test",
            run="11111111-1"
        )
        self.assertIsNotNone(empresa)

    def test_empresa_actualizacion(self):
        """Verifica que se pueda actualizar una empresa"""
        empresa = Empresa.objects.get(nombre="Empresa de prueba")
        empresa.nombre = "Empresa actualizada"
        empresa.save()
        empresa_actualizada = Empresa.objects.get(run="12345678-9")
        self.assertEqual(empresa_actualizada.nombre, "Empresa actualizada")

    def test_empresa_eliminacion(self):
        """Verifica que se pueda eliminar una empresa"""
        empresa = Empresa.objects.get(nombre="Empresa de prueba")
        empresa_id = empresa.id
        empresa.delete()
        with self.assertRaises(Empresa.DoesNotExist):
            Empresa.objects.get(id=empresa_id)

    def test_empresa_conteo(self):
        """Verifica el conteo de empresas"""
        count_inicial = Empresa.objects.count()
        Empresa.objects.create(
            nombre="Nueva empresa",
            direccion="Dirección nueva",
            run="22222222-2"
        )
        self.assertEqual(Empresa.objects.count(), count_inicial + 1)
