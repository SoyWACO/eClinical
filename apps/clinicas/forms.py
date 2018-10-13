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