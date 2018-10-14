# -*- encoding:utf8 -*-
from django import forms
from apps.clinicas.models import Departamento, Clinica

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
				'placeholder':'Nombre del departamento',
				}),
			'descripcion':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Descripción de las funciones que desempeña el departamento',
				}),
		}

class ClinicaForm(forms.ModelForm):

	class Meta:
		model = Clinica
		fields = [
			'nombre',
			'telefono',
			'email',
			'departamento',
			'municipio',
			'direccion',
			'departamentos',
		]
		labels = {
			'nombre':'Nombre',
			'telefono':'Teléfono',
			'email':'Correo electrónico',
			'departamento':'Departamento',
			'municipio':'Municipio',
			'direccion':'Dirección',
			'departamentos':'Departamentos médicos o administrativos',
		}
		help_texts = {
			'nombre':'Obligatorio. Longitud máxima 200 caracteres alfanuméricos.',
			'telefono':'Opcional. Longitud máxima 8 caracteres alfanuméricos.',
			'email':'Opcional.',
			'departamento':'Opcional. Seleccione el departamento donde se ubica la clínica.',
			'municipio':'Opcional. Seleccione el municipio donde se ubica la clínica.',
			'direccion':'Opcional. Longitud máxima 400 caracteres alfanuméricos',
			'departamentos':'Opcional. Seleccione los departamentos médicos o administrativos que posee la clínica.',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Nombre de la clínica',
				}),
			'telefono':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Teléfono de contacto de la clínica',
				}),
			'email':forms.EmailInput(attrs={
				'class':'form-control',
				'placeholder':'Correo electrónico de contacto de la clínica',
				}),
			'departamento':forms.Select(attrs={
				'class':'form-control',
				}),
			'municipio':forms.Select(attrs={
				'class':'form-control',
				}),
			'direccion':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Dirección donde se ubica la clínica',
				}),
			'departamentos':forms.CheckboxSelectMultiple(),
		}