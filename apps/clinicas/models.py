from django.db import models

# Create your models here.

class Departamento(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)