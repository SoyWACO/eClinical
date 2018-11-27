from django.db import models

# Create your models here.


class PruebaEspecial(models.Model):
	codigo = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50, null=True, blank=True)
	des = models.CharField(max_length=50, null=True, blank=True)
	

	def __str__(self):
		return '{}'.format(self.codigo)