# Sale System

## Descripción

Sistema de ventas para una tienda de productos electrónicos.

## Tecnologías utilizadas

- Python
- Django
- Django Rest Framework
- Cloudinary
- Stripe
- Pytest


## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual con Python 3.10 o superior
3. Instalar las dependencias con `pip install -r requirements.txt`
4. Crear un archivo `.env` y agregar las variables de entorno

## Variables de entorno

- `CLOUD_NAME`: Nombre del cloud de Cloudinary
- `API_KEY`: API Key de Cloudinary
- `API_SECRET`: API Secret de Cloudinary

## django rest framework

crear un superusuario
```bash
python manage.py createsuperuser
```

hacer migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

levantar servidor
```bash
python manage.py runserver
```
