from django.contrib import admin
from apps.pais.models import Departamento, Municipio

# Register your models here.

admin.site.register(Departamento)
admin.site.register(Municipio)
