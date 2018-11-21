# -*- encoding:utf8 -*-
from django import forms
from apps.expediente.models import SignoVital

class SignoVitalForm(forms.ModelForm):

	class Meta:
		model = SignoVital
		fields = [
			'temperatura',
			'altura',
			'peso',
			'presion_arterial',
			'pulso_cardiaco',
		]
		labels = {
			'temperatura':'Temperatura',
			'altura':'Altura',
			'peso':'Peso',
			'presion_arterial':'Presión arterial',
			'pulso_cardiaco':'Pulso cardíaco',
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
		}