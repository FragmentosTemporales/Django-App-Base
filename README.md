# DJANGO APP

## APLICACION DE PRUEBA DJANGO

### INSTALACION

1.- Crear entorno virtual con el mítico:
> python -m venv venv

2.- Activar el entorno virtual con el supersensacional:
> source venv/scripts/activate

3.- Instalar requirements.txt
> pip install -r requirements.txt

### CREAR PROYECTO CON DJANGO

1.- Instalar la version de Django con el sencillo:
> pip install django==5.2.7

2.- Crear nuestro primer proyecto con el maravilloso:
> django-admin startproject app .

3.- Crear un modulo
> py manage.py startapp MODULO

### VARIABLES DE ENTORNO

> Las variables de entorno en este proyecto se gestionan con pydantic_settings, sigue el ejemplo de "example.env"

### CREACION DE MIGRACIONES

1.- Para crear una migración debemos ejecutar el siguiente comando:
> py manage.py makemigrations

2.- Para actualizar las migraciones debemos ejecutar el siguiente comando:
> py manage.py migrate

3.- Asegurarse de que la base de datos existe antes de crear el migrate

> bbdd POSTGRESQL de prueba:

```bash
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_db",
        "USER": "postgres",
        "PASSWORD": "Dante123.",
        "HOST": "localhost",
        "PORT": "5432"
    }
}
```

> bbdd SQLite por defecto:

```bash
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}
```

### CREAR ADMINISTRADOR

1.- Para manipular la consola de administrador debes crear un "superusuario"
> py manage.py createsuperuser

### EJECUTAR EL SERVICIO

1.- Para ejecutar el servicio en modo prueba:
> py manage.py runserver
