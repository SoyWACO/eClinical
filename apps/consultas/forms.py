# -*- encoding:utf8 -*-
from django import forms
from apps.consultas.models import ColaEnfermeria, ColaConsulta
from apps.usuarios.models import Usuario
from apps.clinicas.models import Departamento

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

# --------------- COLA DE CONSULTA MEDICA ---------------- #

class ColaConsultaForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		dep = kwargs.pop('departamento', None)
		super().__init__(*args, **kwargs)
		departamento = Departamento.objects.get(pk=dep)
		self.fields['usuario'].queryset = departamento.usuario_set.all()

	class Meta:
		model = ColaConsulta
		fields = [
			'prioridad',
			'clinica',
			'expediente',
			'usuario',
		]
		labels = {
			'prioridad':'Prioridad',
			'clinica':'Clínica',
			'usuario':'Médico',
		}
		help_texts = {
			'prioridad':'Obligatorio. Asigne la prioridad que tendrá el paciente para ser atendido de acuerdo al grado de emergencia.',
			'clinica':'Obligatorio. Indica en qué clínica será atendido el paciente.',
			'usuario':'Obligatorio. Indica el médico que atenderá al paciente.',
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
			'usuario':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Médico',
				'required':'true',
				}),
			'expediente':forms.HiddenInput(),
		}