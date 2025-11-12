from django.test import TestCase
from .models import Producto, Categoria


class CategoriaModelTest(TestCase):
    def setUp(self):
        Categoria.objects.create(nombre="Categoría de prueba")

    def test_categoria_str(self):
        categoria = Categoria.objects.get(nombre="Categoría de prueba")
        self.assertEqual(str(categoria), "Categoría de prueba")


class ProductoModelTest(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nombre="Categoría de prueba")
        values = {
            "nombre": "Producto de prueba",
            "stock": 100,
            "puntaje": 4.5,
            "categoria": categoria
        }
        Producto.objects.create(**values)

    def test_producto_str(self):
        producto = Producto.objects.get(nombre="Producto de prueba")
        self.assertEqual(producto.nombre, "Producto de prueba")

    def test_producto_categoria(self):
        producto = Producto.objects.get(nombre="Producto de prueba")
        self.assertEqual(producto.categoria.nombre, "Categoría de prueba")