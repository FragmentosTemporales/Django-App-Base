from django.test import TestCase
from django.utils import timezone
from .models import Producto, Categoria, EmpresaCategoriaProducto
from empresa.models import Empresa


class CategoriaModelTest(TestCase):
    def setUp(self):
        Categoria.objects.create(nombre="Categoría de prueba")

    def test_categoria_str(self):
        categoria = Categoria.objects.get(nombre="Categoría de prueba")
        self.assertEqual(str(categoria), "Categoría de prueba")

    def test_categoria_creacion_fecha(self):
        """Verifica que se crea el campo creado automáticamente"""
        categoria = Categoria.objects.get(nombre="Categoría de prueba")
        self.assertIsNotNone(categoria.creado)
        self.assertIsInstance(categoria.creado, type(timezone.now()))

    def test_categoria_productos_relacionados(self):
        """Verifica la relación inversa con productos"""
        categoria = Categoria.objects.get(nombre="Categoría de prueba")
        Producto.objects.create(
            nombre="Producto 1",
            stock=10,
            puntaje=4.0,
            categoria=categoria
        )
        Producto.objects.create(
            nombre="Producto 2",
            stock=20,
            puntaje=5.0,
            categoria=categoria
        )
        self.assertEqual(categoria.productos.count(), 2)

    def test_categoria_eliminacion_cascade(self):
        """Verifica que al eliminar una categoría se eliminan sus productos"""
        categoria = Categoria.objects.get(nombre="Categoría de prueba")
        Producto.objects.create(
            nombre="Producto test",
            stock=5,
            puntaje=3.5,
            categoria=categoria
        )
        producto_count = Producto.objects.filter(categoria=categoria).count()
        self.assertGreater(producto_count, 0)
        
        categoria.delete()
        producto_count_despues = Producto.objects.filter(categoria_id=categoria.id).count()
        self.assertEqual(producto_count_despues, 0)


class ProductoModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Categoría de prueba")
        values = {
            "nombre": "Producto de prueba",
            "stock": 100,
            "puntaje": 4.5,
            "categoria": self.categoria
        }
        Producto.objects.create(**values)

    def test_producto_str(self):
        producto = Producto.objects.get(nombre="Producto de prueba")
        self.assertEqual(producto.nombre, "Producto de prueba")

    def test_producto_categoria(self):
        producto = Producto.objects.get(nombre="Producto de prueba")
        self.assertEqual(producto.categoria.nombre, "Categoría de prueba")

    def test_producto_stock_positivo(self):
        """Verifica que el stock pueda ser un número positivo"""
        producto = Producto.objects.get(nombre="Producto de prueba")
        self.assertEqual(producto.stock, 100)
        self.assertGreater(producto.stock, 0)

    def test_producto_stock_cero(self):
        """Verifica que se pueda crear un producto con stock en cero"""
        producto = Producto.objects.create(
            nombre="Producto sin stock",
            stock=0,
            puntaje=3.0,
            categoria=self.categoria
        )
        self.assertEqual(producto.stock, 0)

    def test_producto_puntaje_rango(self):
        """Verifica que el puntaje esté en un rango válido"""
        producto = Producto.objects.get(nombre="Producto de prueba")
        self.assertGreaterEqual(producto.puntaje, 0.0)
        self.assertLessEqual(producto.puntaje, 5.0)

    def test_producto_actualizacion_stock(self):
        """Verifica que se pueda actualizar el stock"""
        producto = Producto.objects.get(nombre="Producto de prueba")
        stock_inicial = producto.stock
        producto.stock = 50
        producto.save()
        producto_actualizado = Producto.objects.get(nombre="Producto de prueba")
        self.assertEqual(producto_actualizado.stock, 50)
        self.assertNotEqual(producto_actualizado.stock, stock_inicial)

    def test_producto_multiples_por_categoria(self):
        """Verifica que una categoría pueda tener múltiples productos"""
        Producto.objects.create(
            nombre="Producto 2",
            stock=200,
            puntaje=3.5,
            categoria=self.categoria
        )
        productos = Producto.objects.filter(categoria=self.categoria)
        self.assertEqual(productos.count(), 2)

    def test_producto_creado_timestamp(self):
        """Verifica que el timestamp de creación se genere correctamente"""
        producto = Producto.objects.get(nombre="Producto de prueba")
        self.assertIsNotNone(producto.creado)
        self.assertLessEqual(producto.creado, timezone.now())


class EmpresaCategoriaProductoModelTest(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(
            nombre="Empresa Test",
            direccion="Calle Test 123",
            run="11111111-1"
        )
        self.categoria = Categoria.objects.create(nombre="Categoría Test")

    def test_empresa_categoria_creacion(self):
        """Verifica la creación de la relación empresa-categoría"""
        relacion = EmpresaCategoriaProducto.objects.create(
            empresa=self.empresa,
            categoria_producto=self.categoria
        )
        self.assertIsNotNone(relacion)
        self.assertEqual(relacion.empresa, self.empresa)
        self.assertEqual(relacion.categoria_producto, self.categoria)

    def test_empresa_categoria_str(self):
        """Verifica el método __str__ de la relación"""
        relacion = EmpresaCategoriaProducto.objects.create(
            empresa=self.empresa,
            categoria_producto=self.categoria
        )
        expected = f"{self.empresa.nombre} - {self.categoria.nombre}"
        self.assertEqual(str(relacion), expected)

    def test_empresa_multiples_categorias(self):
        """Verifica que una empresa pueda tener múltiples categorías"""
        categoria2 = Categoria.objects.create(nombre="Categoría 2")
        
        EmpresaCategoriaProducto.objects.create(
            empresa=self.empresa,
            categoria_producto=self.categoria
        )
        EmpresaCategoriaProducto.objects.create(
            empresa=self.empresa,
            categoria_producto=categoria2
        )
        
        relaciones = EmpresaCategoriaProducto.objects.filter(empresa=self.empresa)
        self.assertEqual(relaciones.count(), 2)

    def test_categoria_multiples_empresas(self):
        """Verifica que una categoría pueda estar asociada a múltiples empresas"""
        empresa2 = Empresa.objects.create(
            nombre="Empresa 2",
            direccion="Calle 2",
            run="22222222-2"
        )
        
        EmpresaCategoriaProducto.objects.create(
            empresa=self.empresa,
            categoria_producto=self.categoria
        )
        EmpresaCategoriaProducto.objects.create(
            empresa=empresa2,
            categoria_producto=self.categoria
        )
        
        relaciones = EmpresaCategoriaProducto.objects.filter(categoria_producto=self.categoria)
        self.assertEqual(relaciones.count(), 2)

    def test_empresa_categoria_cascade_empresa(self):
        """Verifica que al eliminar una empresa se eliminan sus relaciones"""
        EmpresaCategoriaProducto.objects.create(
            empresa=self.empresa,
            categoria_producto=self.categoria
        )
        empresa_id = self.empresa.id
        self.empresa.delete()
        
        relaciones = EmpresaCategoriaProducto.objects.filter(empresa_id=empresa_id)
        self.assertEqual(relaciones.count(), 0)

    def test_empresa_categoria_cascade_categoria(self):
        """Verifica que al eliminar una categoría se eliminan sus relaciones"""
        EmpresaCategoriaProducto.objects.create(
            empresa=self.empresa,
            categoria_producto=self.categoria
        )
        categoria_id = self.categoria.id
        self.categoria.delete()
        
        relaciones = EmpresaCategoriaProducto.objects.filter(categoria_producto_id=categoria_id)
        self.assertEqual(relaciones.count(), 0)
