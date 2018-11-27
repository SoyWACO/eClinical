# -*- encoding:utf8 -*-
from django import forms
from apps.consultas.models import ColaEnfermeria

class ColaEnfermeriaForm(forms.ModelForm):

	class Meta:
		model = ColaEnfermeria
		fields = [
			'prioridad',
		]
		labels = {
			'prioridad':'Prioridad',
		}
		help_texts = {
			'prioridad':'Obligatorio. Longitud máxima 1 caracter alfanuméricos.',
		}
		widgets = {
			'prioridad':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Prioridad',
				}),
		}