from django.db import models

# Create your models here.

# --------------------- DEPARTAMENTO --------------------- #

class Departamento(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.nombre)

# ----------------------- MUNICIPIO ---------------------- #

class Municipio(models.Model):
	nombre = models.CharField(max_length=100)
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.nombre)
