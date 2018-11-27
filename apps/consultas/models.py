from django.db import models
from apps.clinicas.models import Clinica
from apps.expediente.models import Expediente

# Create your models here.

class ColaEnfermeria(models.Model):
	expediente = models.ForeignKey(Expediente, blank=True, on_delete=models.CASCADE)
	clinica = models.ForeignKey(Clinica, blank=True, on_delete=models.CASCADE)
	prioridad = models.CharField(max_length=1)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)