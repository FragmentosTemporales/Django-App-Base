from django.test import TestCase

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
        self.assertEqual(str(empresa.nombre), "Empresa de prueba")
