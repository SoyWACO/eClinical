from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import Group
from apps.usuarios.models import Usuario
from apps.usuarios.forms import GroupForm, UsuarioCreationForm, UsuarioChangeForm

# Create your views here.

# -------------------- ROLES DE USUARIO (GROUPS) -------------------- #

class GroupList(ListView):
	model = Group
	template_name = 'usuarios/rol_list.html'

class GroupCreate(SuccessMessageMixin, CreateView):
	model = Group
	form_class = GroupForm
	template_name = 'usuarios/rol_form.html'
	success_url = reverse_lazy('usuarios:rol_list')
	success_message = 'Rol de usuario %(name)s registrado correctamente'

class GroupUpdate(SuccessMessageMixin, UpdateView):
	model = Group
	form_class = GroupForm
	template_name = 'usuarios/rol_form.html'
	success_url = reverse_lazy('usuarios:rol_list')
	success_message = 'Rol de usuario %(name)s editado correctamente'

class GroupDelete(SuccessMessageMixin, DeleteView):
	model = Group
	template_name = 'usuarios/rol_delete.html'
	success_url = reverse_lazy('usuarios:rol_list')
	success_message = 'Rol de usuario %(name)s eliminado correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(GroupDelete, self).delete(request, *args, **kwargs)

# -------------------- USUARIOS -------------------- #

class UsuarioList(ListView):
	model = Usuario
	template_name = 'usuarios/usuario_list.html'

class UsuarioCreate(SuccessMessageMixin, CreateView):
	model = Usuario
	form_class = UsuarioCreationForm
	template_name = 'usuarios/usuario_form.html'
	success_url = reverse_lazy('usuarios:usuario_list')
	success_message = 'Usuario %(username)s registrado correctamente'

class UsuarioUpdate(SuccessMessageMixin, UpdateView):
	model = Usuario
	form_class = UsuarioChangeForm
	template_name = 'usuarios/usuario_change_form.html'
	success_url = reverse_lazy('usuarios:usuario_list')
	success_message = 'Usuario %(username)s editado correctamente'

class UsuarioDelete(SuccessMessageMixin, DeleteView):
	model = Usuario
	template_name = 'usuarios/usuario_delete.html'
	success_url = reverse_lazy('usuarios:usuario_list')
	success_message = 'Usuario %(username)s eliminado correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(UsuarioDelete, self).delete(request, *args, **kwargs)