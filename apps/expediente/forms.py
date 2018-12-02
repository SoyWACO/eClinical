# -*- encoding:utf8 -*-
from django import forms
from apps.expediente.models import SignoVital, Expediente 

# -------------------- SIGNOS VITALES -------------------- #

class SignoVitalForm(forms.ModelForm):

	class Meta:
		model = SignoVital
		fields = [
			'expediente',
			'temperatura',
			'altura',
			'peso',
			'presion_arterial',
			'pulso_cardiaco',
		]
		labels = {
			'expediente':'Paciente',
			'temperatura':'Temperatura',
			'altura':'Altura',
			'peso':'Peso',
			'presion_arterial':'Presión arterial',
			'pulso_cardiaco':'Pulso cardíaco',
		}
		widgets = {
			'expediente':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Paciente',
				}),
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
		}

# ---------------------- EXPEDIENTE ---------------------- #

class ExpedienteForm(forms.ModelForm):

	class Meta:
		model = Expediente
		fields = [
			'nombre',
			'apellido',
			'fecha_nacimiento',
			'departamento',
			'municipio',
			'direccion',
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
			'fecha_nacimiento':'Fecha de nacimiento',
			'departamento':'Departamento',
			'municipio':'Municipio',
			'direccion':'Dirección',
			'DUI':'DUI',
			'ocupacion':'Ocupación',
			'padre':'Padre',
			'madre':'Madre',
			'conyugue':'Conyugue',
			'estado_civil':'Estado civil',
			'genero':'Género',
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
				'placeholder':'Fecha de nacimiento',
				}),
			'departamento':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Departamento',
				}),
			'municipio':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Municipio',
				}),
			'direccion':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Dirección',
				}),
			'dui':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'DUI',
				}),
			'ocupacion':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Ocupación',
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
			'estado_civil':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Estado civil',
				}),
			'genero':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Género',
				}),
		}
