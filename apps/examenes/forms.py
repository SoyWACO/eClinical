from django import forms
from apps.examenes.models import PruebaEspecial, ExamenSangre, ExamenOrina, ExamenHeces

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



class ExamenOrinaForm(forms.ModelForm):

	class Meta:
		model = ExamenOrina
		fields = [
			'cod',
			'aspecto',
			'color',
			'ph',
			'nitrito',
			'proteinas',
			'glucosa',
			'cuerpo_cetonico',
			'bilirubina',
			'sangre_oculta',
			'leucocitos',
			'hematies',
			'cel_epitelalias',
			'cilindros',
			'parasitos',
			'otros',
			'cristales',
			
		]
		labels = {
			'cod':'Codigo',
			'aspecto':'Aspecto',
			'color':'Color',
			'ph':'PH',
			'nitrito':'Nitrito',
			'proteinas':'Proteinas',
			'glucosa':'Color',
			'cuerpo_cetonico':'Cuerpo cetonico',
			'bilirubina':'Bilirubina',
			'sangre_oculta':'Sangre oculta',
			'leucocitos':'Leucocitos',
			'hematies':'Hematies',
			'cel_epitelalias':'Celulas epitelalias',
			'cilindros':'Cilindros',
			'parasitos':'Parasitos',
			'otros':'Otros',
			'cristales':'Cristales',
			
		}
		widgets = {
			'cod':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Codigo',
				}),
			'aspecto':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Aspecto',
				}),
			'color':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Color',
				}),
			'ph':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'PH',
				}),
			'nitrito':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Nitrito',
				}),
			'proteinas':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Proteinas',
				}),
			'glucosa':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Glucosa',
				}),
			'cuerpo_cetonico':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Cuerpo cetonico',
				}),
			'bilirubina':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Bilirubina',
				}),
			'sangre_oculta':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Sangre oculta',
				}),
			'leucocitos':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Leucocitos',
				}),
			'hematies':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Hematies',
				}),
			'cel_epitelalias':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Celulas epitelalias',
				}),
			'cilindros':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Cilindros',
				}),
			'parasitos':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Parasitos',
				}),
			'otros':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Otros',
				}),
			'cristales':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Cristales',
				}),
		}		

class ExamenHecesForm(forms.ModelForm):

	class Meta:
		model = ExamenHeces
		fields = [
			'cod',
			'color',
			'mucus',
			'leucocitos',
			'hematies',
			'consistencia',
			'res_alimen_macros',
			'res_alimen_micros',
			'levaduras',
			
			
		]
		labels = {
			'cod':'Codigo',
			'color':'Color',
			'mucus':'Mucus',
			'leucocitos':'Leucocitos',
			'hematies':'Hematies',
			'consistencia':'Consistencia',
			'res_alimen_macros':'Restos Alimentos macros',
			'res_alimen_micros':'Restos Alimentos micros',
			'levaduras':'Levaduras',
			
			
		}
		widgets = {
			'cod':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Codigo',
				}),
			'color':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Color',
				}),
			'mucus':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Mucus',
				}),
			'leucocitos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Leucocitos',
				}),
			'hematies':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Hematies',
				}),
			'consistencia':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Consistencia',
				}),
			'res_alimen_macros':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Restos Alimentos macros',
				}),
			'res_alimen_micros':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Restos Alimentos micros',
				}),
			'levaduras':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Levaduras',
				}),
			
		}		