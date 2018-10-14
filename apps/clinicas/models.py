from django.db import models
from apps.pais.models import Departamento, Municipio

# Create your models here.

class Departamento(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)

class Clinica(models.Model):
	nombre = models.CharField(max_length=200)
	telefono = models.CharField(max_length=8)
	email = models.EmailField()
	departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
	municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)
	direccion = models.CharField(max_length=400)