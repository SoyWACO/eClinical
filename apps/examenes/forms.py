from django import forms
from apps.examenes.models import PruebaEspecial 

class PruebaEspecialForm(forms.ModelForm):

	class Meta:
		model = PruebaEspecial
		fields = [
			'codigo',
			'tipo',
			'des',
			
		]
		labels = {
			'codigo':'Codigo',
			'tipo':'Tipo',
			'des':'Descripcion',
			
		}
		widgets = {
			'codigo':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Codigo',
				}),
			'tipo':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Tipo',
				}),
			'des':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Descripcion',
				}),
			
		}