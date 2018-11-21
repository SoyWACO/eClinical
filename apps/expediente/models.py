from django.db import models

# Create your models here.

class SignoVital(models.Model):
	temperatura = models.IntegerField(null=True, blank=True)
	altura = models.IntegerField()
	peso = models.IntegerField()
	presion_arterial = models.CharField(max_length=7, null=True, blank=True)
	pulso_cardiaco = models.IntegerField(null=True, blank=True)
