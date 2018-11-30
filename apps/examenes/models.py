from django.db import models

# Create your models here.


class PruebaEspecial(models.Model):
	codigo = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50, null=True, blank=True)
	des = models.CharField(max_length=50, null=True, blank=True)
	

	def __str__(self):
		return '{}'.format(self.codigo)


class ExamenSangre(models.Model):
	cod = models.CharField(max_length=50)
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
	eucinofilos = models.IntegerField(null=True, blank=True)
	basofilos = models.IntegerField(null=True, blank=True)

#-------------------------------------------------------------------
class ExamenOrina(models.Model):
	cod = models.CharField(max_length=10)
	aspecto = models.CharField(max_length=50, null=True, blank=True)
	color = models.CharField(max_length=50,null=True, blank=True)
	ph = models.IntegerField(null=True, blank=True)
	nitrito = models.CharField(max_length=50,null=True, blank=True)
	proteinas= models.IntegerField(null=True, blank=True)
	glucosa = models.IntegerField(null=True, blank=True)
	cuerpo_cetonico = models.CharField(max_length=50, null=True, blank=True)
	bilirubina = models.CharField(max_length=50, null=True, blank=True)
	sangre_oculta = models.IntegerField(null=True, blank=True)
	leucocitos = models.CharField(max_length=50, null=True, blank=True)
	hematies = models.CharField(max_length=50, null=True, blank=True)
	cel_epitelalias = models.CharField(max_length=50, null=True, blank=True)
	cilindros = models.CharField(max_length=50, null=True, blank=True)
	parasitos= models.CharField(max_length=50, null=True, blank=True)
	otros = models.CharField(max_length=50, null=True, blank=True)
	cristales = models.CharField(max_length=50, null=True, blank=True)
	

#---------------------------------------------------------------

class ExamenHeces(models.Model):
	cod = models.CharField(max_length=10)
	color = models.CharField(max_length=50,null=True, blank=True)
	mucus = models.CharField(max_length=50,null=True, blank=True)
	leucocitos= models.CharField(max_length=50, null=True, blank=True)
	hematies = models.CharField(max_length=50, null=True, blank=True)
	consistencia = models.CharField(max_length=50, null=True, blank=True)
	res_alimen_macros = models.CharField(max_length=50, null=True, blank=True)
	res_alimen_micros = models.CharField(max_length=50, null=True, blank=True)
	levaduras = models.CharField(max_length=50, null=True, blank=True)
	
	
