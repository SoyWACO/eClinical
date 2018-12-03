from django import forms
from apps.examenes.models import PruebaEspecial, ExamenSangre, ExamenOrina, ExamenHeces, ExamenFisico

# -------------------- PRUEBA ESPECIAL ------------------- #

class PruebaEspecialForm(forms.ModelForm):

	class Meta:
		model = PruebaEspecial
		fields = [
			'expediente',
			'usuario',
			'observaciones',
		]
		labels = {
			'expediente':'Paciente',
			'usuario':'Médico',
			'observaciones':'Observaciones',
		}
		widgets = {
			'expediente':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Paciente',
				}),
			'usuario':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Médico',
				}),
			'observaciones':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Observaciones',
				}),
		}

# -------------- EXAMEN DE QUIMICA SANGUINEA ------------- #

class ExamenSangreForm(forms.ModelForm):

	class Meta:
		model = ExamenSangre
		fields = [
			'expediente',
			'usuario',
			'rbc',
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
			'eosinofilos',
			'basofilos',
			'observaciones',
		]
		labels = {
			'expediente':'Paciente',
			'usuario':'Médico',
			'rbc':'RBC',
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
			'eosinofilos':'Eosinofilos',
			'basofilos':'Basofilos',
			'observaciones':'Observaciones',
		}
		widgets = {
			'expediente':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Paciente',
				}),
			'usuario':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Médico',
				}),
			'rbc':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'RBC',
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
			'eosinofilos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Eosinofilos',
				}),
			'basofilos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Basofilos',
				}),
			'observaciones':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Observaciones',
				}),
		}		

# -------------------- EXAMEN DE ORINA ------------------- #

class ExamenOrinaForm(forms.ModelForm):

	class Meta:
		model = ExamenOrina
		fields = [
			'expediente',
			'usuario',
			'aspecto',
			'color',
			'ph',
			'densidad',
			'esteraza_leucocitaria',
			'nitritos',
			'proteinas',
			'glucosa',
			'cuerpos_cetonicos',
			'urobilinogeno',
			'bilirrubina',
			'sangre_oculta',
			'leucocitos',
			'hematies',
			'cilindros',
			'cristales',
			'parasitos',
			'otros',
			'observaciones',
		]
		labels = {
			'expediente':'Paciente',
			'usuario':'Médico',
			'aspecto':'Aspecto',
			'color':'Color',
			'ph':'PH',
			'densidad':'Densidad',
			'esteraza_leucocitaria':'Esteraza leucocitaria',
			'nitritos':'Nitritos',
			'proteinas':'Proteínas',
			'glucosa':'Glucosa',
			'cuerpos_cetonicos':'Cuerpos cetónicos',
			'urobilinogeno':'Urobilinógeno',
			'bilirrubina':'Bilirrubina',
			'sangre_oculta':'Sangre oculta',
			'leucocitos':'Leucocitos',
			'hematies':'Hematies',
			'cilindros':'Cilindros',
			'cristales':'Cristales',
			'parasitos':'Parásitos',
			'otros':'Otros',
			'observaciones':'Observaciones',
		}
		widgets = {
			'expediente':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Paciente',
				}),
			'usuario':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Médico',
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
			'densidad':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Densidad',
				}),
			'esteraza_leucocitaria':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Esteraza leucocitaria',
				}),
			'nitritos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Nitritos',
				}),
			'proteinas':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Proteínas',
				}),
			'glucosa':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Glucosa',
				}),
			'cuerpos_cetonicos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Cuerpos cetónicos',
				}),
			'urobilinogeno':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Urobilinógeno',
				}),
			'bilirrubina':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Bilirrubina',
				}),
			'sangre_oculta':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Sangre oculta',
				}),
			'leucocitos':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Leucocitos',
				}),
			'hematies':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Hematies',
				}),
			'cilindros':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Cilindros',
				}),
			'cristales':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Cristales',
				}),
			'parasitos':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Parásitos',
				}),
			'otros':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Otros',
				}),
			'observaciones':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Observaciones',
				}),
		}		

# -------------------- EXAMEN DE HECES ------------------- #

class ExamenHecesForm(forms.ModelForm):

	class Meta:
		model = ExamenHeces
		fields = [
			'expediente',
			'usuario',
			'color',
			'mucus',
			'leucocitos',
			'hematies',
			'consistencia',
			'res_alimen_macros',
			'res_alimen_micros',
			'levaduras',
			'protozoarios',
			'metazoarios',
			'observaciones',
		]
		labels = {
			'expediente':'Paciente',
			'usuario':'Médico',
			'color':'Color',
			'mucus':'Mucus',
			'leucocitos':'Leucocitos',
			'hematies':'Hematies',
			'consistencia':'Consistencia',
			'res_alimen_macros':'Restos alimenticios macroscópicos',
			'res_alimen_micros':'Restos alimenticios microscópicos',
			'levaduras':'Levaduras',
			'protozoarios':'Protozoarios',
			'metazoarios':'Metazoarios',
			'observaciones':'Observaciones',
		}
		widgets = {
			'expediente':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Paciente',
				}),
			'usuario':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Médico',
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
			'consistencia':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Consistencia',
				}),
			'res_alimen_macros':forms.TextInput(attrs={
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
			'protozoarios':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Protozoarios',
				}),
			'metazoarios':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Metazoarios',
				}),
			'observaciones':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Observaciones',
				}),
		}

# --------------------- EXAMEN FISICO -------------------- #

class ExamenFisicoForm(forms.ModelForm):

	class Meta:
		model = ExamenFisico
		fields = [
			'expediente',
			'usuario',
			'tipo',
			'imagen',
			'observaciones',
		]
		labels = {
			'expediente':'Expediente',
			'usuario':'Usuario',
			'tipo':'Tipo de examen',
			'imagen':'Imagen',
			'observaciones':'Observaciones',
		}
		widgets = {
			'expediente':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Paciente',
				}),
			'usuario':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Médico',
				}),
			'tipo':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Tipo de examen',
				}),
			'imagen':forms.FileInput(attrs={
				'class':'form-control',
				}),
			'observaciones':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Observaciones',
				}),
		}
