from django.db import models
from apps.clinicas.models import Clinica
from apps.expediente.models import Expediente
from apps.usuarios.models import Usuario

# Create your models here.

# ------------------ COLA DE ENFERMERIA ------------------ #

class ColaEnfermeria(models.Model):
	PRIORIDAD_CHOICES = (
		('A', 'Alta'),
		('B', 'Media'),
		('C', 'Baja'),
	)
	expediente = models.ForeignKey(Expediente, blank=True, on_delete=models.CASCADE)
	clinica = models.ForeignKey(Clinica, blank=True, on_delete=models.CASCADE)
	prioridad = models.CharField(max_length=1, choices=PRIORIDAD_CHOICES)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)

# --------------- COLA DE CONSULTA MEDICA ---------------- #

class ColaConsulta(models.Model):
	PRIORIDAD_CHOICES = (
		('A', 'Alta'),
		('B', 'Media'),
		('C', 'Baja'),
	)
	expediente = models.ForeignKey(Expediente, blank=True, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL) # Médico
	clinica = models.ForeignKey(Clinica, blank=True, on_delete=models.CASCADE)
	prioridad = models.CharField(max_length=1, choices=PRIORIDAD_CHOICES)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)

# ------------------- CONSULTAS MÉDICAS ------------------ #

class ConsultaMedica(models.Model):
	expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE) # Paciente
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL) # Médico
	sintomatologia = models.TextField(null=True, blank=True)
	diagnostico = models.TextField(null=True, blank=True)
	tratamiento = models.TextField(null=True, blank=True)
	medicamentos = models.TextField(null=True, blank=True)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)