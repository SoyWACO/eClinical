from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.clinicas.models import Clinica, Departamento

# Create your models here.

# ---------------------- USUARIO ---------------------- #

class Usuario(AbstractUser, models.Model):
	clinica = models.ForeignKey(Clinica, null=True, blank=True, on_delete=models.SET_NULL)
	departamentos = models.ManyToManyField(Departamento, blank=True)

	def __str__(self):
		return self.username