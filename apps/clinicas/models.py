from django.db import models
from apps.pais.models import Departamento as Dep, Municipio

# Create your models here.

# --------------------- DEPARTAMENTO --------------------- #

class Departamento(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)

# ------------------------ CLINICA ----------------------- #

class Clinica(models.Model):
	nombre = models.CharField(max_length=200)
	telefono = models.CharField(max_length=8, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	departamento = models.ForeignKey(Dep, null=True, blank=True, on_delete=models.SET_NULL)
	municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.SET_NULL)
	direccion = models.TextField(null=True, blank=True)
	departamentos = models.ManyToManyField(Departamento, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)