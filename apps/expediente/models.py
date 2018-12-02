from django.db import models
from apps.pais.models import Departamento as Dep, Municipio
# Create your models here.

class SignoVital(models.Model):
	temperatura = models.IntegerField(null=True, blank=True)
	altura = models.IntegerField()
	peso = models.IntegerField()
	presion_arterial = models.CharField(max_length=7, null=True, blank=True)
	pulso_cardiaco = models.IntegerField(null=True, blank=True)
	fecha=models.DateField(auto_now=False,auto_now_add=False)


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
	DUI = models.CharField(max_length=10, null=True, blank=True)
	ocupacion=models.CharField(max_length=250,null=True,blank=True)
	padre=models.CharField(max_length=200,null=True,blank=True)
	madre=models.CharField(max_length=200,null=True,blank=True)
	conyugue=models.CharField(max_length=200,null=True,blank=True)
	estado_civil=models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, null=True, blank=True)
	genero=models.CharField(max_length=1, choices=GENEROS_CHOICES)