from django import forms
from apps.examenes.models import PruebaEspecial, ExamenSangre

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

class ExamenSangreForm(forms.ModelForm):

	class Meta:
		model = ExamenSangre
		fields = [
			'cod',
			'hemoglobina',
			'hematocrito',
			'mvc',
			'mch',
			'mchc',
			'plaquetas',
			'mpv',
			'pdw',
			'leucocitos',
			'neutrofilos',
			'linfocitos',
			'monocitos',
			'eucinofilos',
			'basofilos',
			
			
		]
		labels = {
			'cod':'Codigo',
			'hemoglobina':'Hemoglobina',
			'hematocrito':'Hematocrito',
			'mvc':'MVC',
			'mch':'MCH',
			'mchc':'MCHC',
			'plaquetas':'Plaquetas',
			'mpv':'MVP',
			'pdw':'PDW',
			'leucocitos':'Leucocitos',
			'neutrofilos':'Neutrofilos',
			'linfocitos':'Linfocitos',
			'monocitos':'Monocitos',
			'eucinofilos':'Eucinofilos',
			'basofilos':'Basofilos',
			
		}
		widgets = {
			'cod':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Codigo',
				}),
			'hemoglobina':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Hemoglobina',
				}),
			'hematocrito':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Hematocrito',
				}),
			'mvc':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'MVC',
				}),
			'mch':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'MCH',
				}),
			'mchc':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'MCHC',
				}),
			'plaquetas':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Plaquetas',
				}),
			'mpv':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'MVP',
				}),
			'pdw':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'PDW',
				}),
			'leucocitos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Leucocitos',
				}),
			'neutrofilos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Neutrofilos',
				}),
			'linfocitos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Linfocitos',
				}),
			'monocitos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Monocitos',
				}),
			'eucinofilos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Eucinofilos',
				}),
			'basofilos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Basofilos',
				}),
		}		