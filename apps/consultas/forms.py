# -*- encoding:utf8 -*-
from django import forms
from apps.consultas.models import ColaEnfermeria

# ------------------ COLA DE ENFERMERIA ------------------ #

class ColaEnfermeriaForm(forms.ModelForm):

	class Meta:
		model = ColaEnfermeria
		fields = [
			'prioridad',
			'clinica',
			'expediente',
		]
		labels = {
			'prioridad':'Prioridad',
			'clinica':'Clínica',
		}
		help_texts = {
			'prioridad':'Obligatorio. Asigne la prioridad que tendrá el paciente para ser atendido de acuerdo al grado de emergencia.',
			'clinica':'Obligatorio. Indica en qué clínica será atendido el paciente.',
		}
		widgets = {
			'prioridad':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Prioridad',
				}),
			'clinica':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Clínica',
				}),
			'expediente':forms.HiddenInput(),
		}
