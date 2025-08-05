# Base de datos

Por defecto, la aplicación está configurada para usar PostgreSQL, ideal para despliegue en Render.

## Configuración local

1. Instala PostgreSQL y crea una base de datos y usuario.
2. Crea un archivo `.env` en la raíz del proyecto con:

    DATABASE_URL=postgresql+psycopg2://usuario:contraseña@localhost:5432/nombre_db

3. Instala las dependencias:
    pip install -r requirements.txt

## Despliegue en Render

Render provee la variable de entorno `DATABASE_URL` automáticamente. No necesitas cambiar nada en el código.

## Migración desde SQLite

Si tienes datos en SQLite y necesitas migrarlos, puedes usar herramientas como `pgloader` o scripts personalizados.
