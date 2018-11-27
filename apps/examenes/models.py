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


	
