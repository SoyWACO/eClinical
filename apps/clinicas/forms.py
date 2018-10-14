# -*- encoding:utf8 -*-
from django import forms
from apps.clinicas.models import Departamento

class DepartamentoForm(forms.ModelForm):

	class Meta:
		model = Departamento
		fields = [
			'nombre',
			'descripcion',
		]
		labels = {
			'nombre':'Nombre',
			'descripcion':'Descripción',
		}
		help_texts = {
			'nombre':'Obligatorio. Longitud máxima 200 caracteres alfanuméricos.',
			'descripcion':'Opcional. Breve explicación de la función que desempeña el departamento.',
		}
		error_messages = {
			'nombre':{'max_length':('Longitud máxima 200 caracteres alfanuméricos.')},
		}
		widgets = {
			'nombre':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Nombre',
				}),
			'descripcion':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Descripción',
				}),
		}