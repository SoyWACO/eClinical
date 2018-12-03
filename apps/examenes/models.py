from django.db import models
from apps.expediente.models import Expediente
from apps.usuarios.models import Usuario

# Create your models here.

# -------------------- PRUEBA ESPECIAL ------------------- #

class PruebaEspecial(models.Model):
	expediente = models.ForeignKey(Expediente, blank=True, on_delete=models.CASCADE) # Paciente
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL) # Médico
	observaciones = models.TextField(null=True, blank=True)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)

# -------------- EXAMEN DE QUIMICA SANGUINEA ------------- #

class ExamenSangre(models.Model):
	expediente = models.ForeignKey(Expediente, blank=True, on_delete=models.CASCADE) # Paciente
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL) # Médico
	rbc = models.IntegerField(null=True, blank=True)
	hemoglobina = models.IntegerField(null=True, blank=True)
	hematocrito = models.IntegerField(null=True, blank=True)
	mvc = models.IntegerField(null=True, blank=True)
	mch = models.IntegerField(null=True, blank=True)
	mchc = models.IntegerField(null=True, blank=True)
	plaquetas = models.IntegerField(null=True, blank=True)
	mpv = models.IntegerField(null=True, blank=True)
	pdw = models.IntegerField(null=True, blank=True)
	leucocitos = models.IntegerField(null=True, blank=True)
	neutrofilos = models.IntegerField(null=True, blank=True)
	linfocitos = models.IntegerField(null=True, blank=True)
	monocitos = models.IntegerField(null=True, blank=True)
	eosinofilos = models.IntegerField(null=True, blank=True)
	basofilos = models.IntegerField(null=True, blank=True)
	observaciones = models.TextField(null=True, blank=True)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)

# -------------------- EXAMEN DE ORINA ------------------- #

class ExamenOrina(models.Model):
	expediente = models.ForeignKey(Expediente, blank=True, on_delete=models.CASCADE) # Paciente
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL) # Médico
	aspecto = models.CharField(max_length=50, null=True, blank=True)
	color = models.CharField(max_length=50,null=True, blank=True)
	ph = models.IntegerField(null=True, blank=True)
	densidad = models.IntegerField(null=True, blank=True)
	esteraza_leucocitaria = models.IntegerField(null=True, blank=True)
	nitritos = models.IntegerField(null=True, blank=True)
	proteinas = models.IntegerField(null=True, blank=True)
	glucosa = models.IntegerField(null=True, blank=True)
	cuerpos_cetonicos = models.IntegerField(null=True, blank=True)
	urobilinogeno = models.IntegerField(null=True, blank=True)
	bilirrubina = models.IntegerField(null=True, blank=True)
	sangre_oculta = models.IntegerField(null=True, blank=True)
	leucocitos = models.IntegerField(null=True, blank=True)
	hematies = models.IntegerField(null=True, blank=True)
	cilindros = models.CharField(max_length=100, null=True, blank=True)
	cristales = models.CharField(max_length=100, null=True, blank=True)
	parasitos = models.CharField(max_length=100, null=True, blank=True)
	otros = models.CharField(max_length=100, null=True, blank=True)
	observaciones = models.TextField(null=True, blank=True)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)

# -------------------- EXAMEN DE HECES ------------------- #

class ExamenHeces(models.Model):
	ESTADO_CHOICES = (
		('Q', 'Quistes'),
		('A', 'Activos'),
	)
	expediente = models.ForeignKey(Expediente, blank=True, on_delete=models.CASCADE) # Paciente
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL) # Médico
	color = models.CharField(max_length=50,null=True, blank=True)
	mucus = models.CharField(max_length=50,null=True, blank=True)
	leucocitos= models.IntegerField(null=True, blank=True)
	hematies = models.IntegerField(null=True, blank=True)
	consistencia = models.CharField(max_length=50, null=True, blank=True)
	res_alimen_macros = models.CharField(max_length=50, null=True, blank=True)
	res_alimen_micros = models.CharField(max_length=50, null=True, blank=True)
	levaduras = models.CharField(max_length=50, null=True, blank=True)
	protozoarios = models.CharField(max_length=1, choices=ESTADO_CHOICES, null=True, blank=True)
	metazoarios = models.CharField(max_length=1, choices=ESTADO_CHOICES, null=True, blank=True)
	observaciones = models.TextField(null=True, blank=True)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)

# --------------------- EXAMEN FISICO -------------------- #

class ExamenFisico(models.Model):
	expediente = models.ForeignKey(Expediente, blank=True, on_delete=models.CASCADE) # Paciente
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL) # Médico
	tipo = models.CharField(max_length=100, null=True, blank=True)
	imagen  = models.ImageField(upload_to='examenes')
	observaciones = models.TextField(null=True, blank=True)
	fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)