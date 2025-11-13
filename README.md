# Django App Base

Aplicación base de Django con GraphQL, gestión de empresas y productos, lista para desarrollo y producción.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Testing](#testing)
- [API GraphQL](#api-graphql)
- [Modelos de Datos](#modelos-de-datos)
- [Contribuir](#contribuir)

## ✨ Características

- **Django 5.2.7**: Framework web robusto y escalable
- **GraphQL API**: Implementado con Graphene-Django
- **Base de Datos**: Compatible con PostgreSQL y SQLite
- **Apps Modulares**:
  - `empresa`: Gestión de empresas con RUN único
  - `productos`: Gestión de productos, categorías y relaciones
- **Variables de Entorno**: Configuración segura con Pydantic Settings
- **Tests Unitarios**: Cobertura completa de modelos (26 tests)
- **Admin Panel**: Panel de administración de Django configurado

## 📦 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- PostgreSQL (opcional, puede usar SQLite)
- Git

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/FragmentosTemporales/Django-App-Base.git
cd Django-App-Base
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## ⚙️ Configuración

### Variables de Entorno

El proyecto utiliza `pydantic_settings` para gestionar las variables de entorno de forma segura.

1. Crea un archivo `.env` en la raíz del proyecto basándote en `example.env`:

```env
# Configuración de Django
DEBUG=True
SECRET_KEY=tu-clave-secreta-aqui
ALLOWED_HOSTS=localhost,127.0.0.1

# Configuración de Base de Datos
DB_ENGINE=django.db.backends.postgresql
DB_NAME=django_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

### Base de Datos

#### Opción 1: PostgreSQL (Recomendado para producción)

1. Crear la base de datos:
```sql
CREATE DATABASE django_db;
```

2. Configurar en `settings.py`:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_db",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432"
    }
}
```

#### Opción 2: SQLite (Para desarrollo)

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### Migraciones

1. Crear archivos de migración:
```bash
python manage.py makemigrations
```

2. Aplicar migraciones a la base de datos:
```bash
python manage.py migrate
```

### Crear Superusuario

Para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear tu usuario administrador.

## 📁 Estructura del Proyecto

```
Django-App-Base/
├── app/                      # Configuración principal del proyecto
│   ├── models/              # Modelos base compartidos
│   ├── static/              # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/           # Plantillas HTML base
│   ├── settings.py          # Configuración de Django
│   ├── urls.py              # URLs principales
│   └── schema.py            # Schema principal de GraphQL
├── empresa/                 # App de gestión de empresas
│   ├── models.py            # Modelo Empresa
│   ├── schemas/             # Queries y mutations de GraphQL
│   ├── tests.py             # Tests unitarios
│   └── migrations/          # Migraciones de base de datos
├── productos/               # App de gestión de productos
│   ├── models.py            # Modelos Producto, Categoría, etc.
│   ├── schemas/             # Queries y mutations de GraphQL
│   ├── templates/           # Plantillas específicas
│   ├── tests.py             # Tests unitarios
│   └── migrations/          # Migraciones de base de datos
├── manage.py                # Script de gestión de Django
├── requirements.txt         # Dependencias del proyecto
└── README.md               # Este archivo
```

## 🎯 Uso

### Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

### Acceder al Panel de Administración

1. Navega a: `http://localhost:8000/admin`
2. Inicia sesión con el superusuario creado anteriormente

### Acceder a GraphiQL (GraphQL IDE)

Navega a: `http://localhost:8000/graphql`

## 🧪 Testing

### Ejecutar todos los tests

```bash
python manage.py test
```

### Ejecutar tests con verbosidad

```bash
python manage.py test -v 2
```

### Ejecutar tests de una app específica

```bash
python manage.py test empresa
python manage.py test productos
```

### Ejecutar un test específico

```bash
python manage.py test productos.tests.ProductoModelTest.test_producto_stock_positivo
```

### Cobertura de Tests

El proyecto cuenta con **26 tests unitarios** que cubren:
- ✅ Validación de modelos
- ✅ Relaciones entre entidades
- ✅ Restricciones de base de datos
- ✅ Eliminación en cascada
- ✅ Actualizaciones de datos
- ✅ Campos únicos y opcionales

## 🔌 API GraphQL

### Ejemplos de Queries

#### Listar todas las empresas

```graphql
query {
  allEmpresas {
    id
    nombre
    run
    direccion
    website
    creado
  }
}
```

#### Listar productos con categoría

```graphql
query {
  allProductos {
    id
    nombre
    stock
    puntaje
    categoria {
      id
      nombre
    }
  }
}
```

### Ejemplos de Mutations

#### Crear una empresa

```graphql
mutation {
  createEmpresa(input: {
    nombre: "Mi Empresa"
    run: "12345678-9"
    direccion: "Calle Principal 123"
    website: "https://miempresa.com"
  }) {
    empresa {
      id
      nombre
    }
  }
}
```

#### Crear un producto

```graphql
mutation {
  createProducto(input: {
    nombre: "Nuevo Producto"
    stock: 100
    puntaje: 4.5
    categoriaId: 1
  }) {
    producto {
      id
      nombre
      stock
    }
  }
}
```

## 📊 Modelos de Datos

### Empresa
- `nombre`: CharField (max_length=255)
- `run`: CharField (max_length=20, unique=True)
- `direccion`: CharField (max_length=255)
- `website`: URLField (opcional)
- `creado`: DateTimeField (auto_now_add=True)

### Categoría
- `nombre`: CharField (max_length=255)
- `creado`: DateTimeField (auto_now_add=True)

### Producto
- `nombre`: CharField (max_length=100)
- `stock`: IntegerField
- `puntaje`: FloatField
- `categoria`: ForeignKey → Categoría
- `creado`: DateTimeField (auto_now_add=True)

### EmpresaCategoriaProducto
- `empresa`: ForeignKey → Empresa
- `categoria_producto`: ForeignKey → Categoría
- `creado`: DateTimeField (auto_now_add=True)

## 🛠️ Comandos Útiles de Django

### Crear una nueva app

```bash
python manage.py startapp nombre_app
```

### Abrir shell de Django

```bash
python manage.py shell
```

### Recopilar archivos estáticos

```bash
python manage.py collectstatic
```

### Verificar el proyecto

```bash
python manage.py check
```

### Ver SQL de las migraciones

```bash
python manage.py sqlmigrate app_name 0001
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Notas Adicionales

- Asegúrate de que la base de datos existe antes de ejecutar las migraciones
- Las variables de entorno son esenciales para el funcionamiento en producción
- El campo `run` en el modelo Empresa debe ser único
- Los tests se ejecutan en una base de datos temporal separada

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y comercial.

---

**Desarrollado con ❤️ usando Django**
