from django.db import models
from apps.pais.models import Departamento as Dep, Municipio

# Create your models here.

# ---------------------- EXPEDIENTE ---------------------- #

class Expediente(models.Model):
	GENEROS_CHOICES = (
		('F', 'Femenino'),
		('M', 'Masculino'),
	)
	ESTADO_CIVIL_CHOICES = (
		('C', 'Casado/a'),
		('D', 'Divorciado/a'),
		('S', 'Soltero/a'),
		('V', 'Viudo/a'),
	)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField(auto_now=False,auto_now_add=False)
	departamento = models.ForeignKey(Dep, null=True, blank=True, on_delete=models.SET_NULL)
	municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.SET_NULL)
	direccion = models.TextField(null=True, blank=True)
	DUI = models.CharField(max_length=10, null=True, blank=True)
	ocupacion = models.CharField(max_length=250,null=True,blank=True)
	padre = models.CharField(max_length=200,null=True,blank=True)
	madre = models.CharField(max_length=200,null=True,blank=True)
	conyugue = models.CharField(max_length=200,null=True,blank=True)
	estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, null=True, blank=True)
	genero = models.CharField(max_length=1, choices=GENEROS_CHOICES)

	def __str__(self):
		return self.nombre + " " + self.apellido

# -------------------- SIGNOS VITALES -------------------- #

class SignoVital(models.Model):
	expediente = models.ForeignKey(Expediente, blank=True, on_delete=models.CASCADE)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)
	temperatura = models.IntegerField(null=True, blank=True)
	altura = models.IntegerField()
	peso = models.IntegerField()
	presion_arterial = models.CharField(max_length=7, null=True, blank=True)
	pulso_cardiaco = models.IntegerField(null=True, blank=True)	