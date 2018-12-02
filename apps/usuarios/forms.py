# -*- encoding:utf8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = Usuario
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'groups',
			'clinica',
			'departamentos',
		]
		widgets = {
			'groups':forms.SelectMultiple(attrs={
				'class':'form-control',
				'placeholder':'Roles de Usuario',
				}),
			'clinica':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Clínica',
				}),
			'departamentos':forms.SelectMultiple(attrs={
				'class':'form-control',
				'placeholder':'Departamentos médicos o administrativos',
				}),
		}

class UsuarioChangeForm(UserChangeForm):

	class Meta:
		model = Usuario
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'groups',
			'clinica',
			'departamentos',
		]
		widgets = {
			'groups':forms.SelectMultiple(attrs={
				'class':'form-control',
				'placeholder':'Roles de Usuario',
				}),
			'clinica':forms.Select(attrs={
				'class':'form-control',
				'placeholder':'Clínica',
				}),
			'departamentos':forms.SelectMultiple(attrs={
				'class':'form-control',
				'placeholder':'Departamentos médicos o administrativos',
				}),
		}

class GroupForm(forms.ModelForm):

	class Meta:
		model = Group
		fields = [
			'name',
			'permissions',
		]
		labels = {
			'name':'Rol de usuario',
			'permissions':'Permisos',
		}
		help_texts = {
			'name':'Obligatorio. Longitud máxima 80 caracteres alfanuméricos.',
			'permissions':'Opcional. Seleccione los permisos que corresponden al rol de usuario.',
		}
		error_messages = {
			'name':{'max_length':('Longitud máxima 80 caracteres alfanuméricos.')},
		}
		widgets = {
			'name':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Nombre del rol de usuario',
				}),
			'permissions':forms.CheckboxSelectMultiple(),
		}