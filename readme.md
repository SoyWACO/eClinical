# eClinical

*Expediente clínico para el proyecto de la asignatura Tecnología Orientada a Objetos (TOO115).*

## Requerimientos

- Django 2.1
- Mysqlclient (para Windows)

> [Tutorial para instalar mysqlclient](https://www.pythoniza.me/instalando-mysqlclient-en-windows/)
> [Página para descargar mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)


## Base de datos

1. Crear una base de datos llamada eclinical.

2. Modificar en `eClinical/settings.py` en el diccionario `DATABASES` los campos `USER` y `PASSWORD`, según necesidades.

> Las que aparecen son las credenciales por defecto en XAMPP.

3. Crear las migraciones.

```bash
manage.py makemigrations
```

4. Migrar a la base de datos.

```bash
manage.py migrate
```

5. Correr el servidor.

```bash
manage.py runserver
```