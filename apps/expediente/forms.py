# -*- encoding:utf8 -*-
from django import forms
from apps.expediente.models import SignoVital, Expediente 

class SignoVitalForm(forms.ModelForm):

	class Meta:
		model = SignoVital
		fields = [
			'temperatura',
			'altura',
			'peso',
			'presion_arterial',
			'pulso_cardiaco',
			'fecha',
		]
		labels = {
			'temperatura':'Temperatura',
			'altura':'Altura',
			'peso':'Peso',
			'presion_arterial':'Presión arterial',
			'pulso_cardiaco':'Pulso cardíaco',
			'fecha':'Fecha',
		}
		widgets = {
			'temperatura':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Temperatura',
				}),
			'altura':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Altura',
				}),
			'peso':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Peso',
				}),
			'presion_arterial':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Presión arterial',
				}),
			'pulso_cardiaco':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Pulso cardíaco',
				}),
			'fecha':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Fecha',
				}),
		}

#---------------------formulario expediente--------------------------#
class ExpedienteForm(forms.ModelForm):

	class Meta:
		model = Expediente
		fields = [
			'nombre',
			'apellido',
			'fecha_nacimiento',
			'departamento',
			'municipio',
			'DUI',
			'ocupacion',
			'padre',
			'madre',
			'conyugue',
			'estado_civil',
			'genero',
		]
		labels = {
			'nombre':'Nombre', 
			'apellido':'Apellido',
			'fecha_nacimiento':'Fecha nacimiento',
			'departamento':'Departamento',
			'municipio':'Municipio',
			'DUI':'DUI',
			'ocupacion':'Ocupacion',
			'padre':'Padre',
			'madre':'Madre',
			'conyugue':'Conyugue',
			'estado_civil':'Estado civil',
			'genero':'genero',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Nombre',
				}),
			'apellido':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Apellido',
				}),
			'fecha_nacimiento':forms.DateInput(attrs={
				'class':'form-control',
				'placeholder':'Fecha nacimiento',
				}),
			'departamento':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Departamento',
				}),
			'municipio':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Municipio',
				}),
			'DUI':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'DUI',
				}),
			'ocupacion':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Ocupacion',
				}),
			'padre':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Padre',
				}),
			'madre':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Madre',
				}),
			'conyugue':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Conyugue',
				}),
			'estado_civil':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Estado civil',
				}),
			'genero':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Genero',
				}),
		}