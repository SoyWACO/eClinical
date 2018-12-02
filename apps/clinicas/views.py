from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.clinicas.models import Departamento, Clinica
from apps.clinicas.forms import DepartamentoForm, ClinicaForm

# Create your views here.

# -------------------- DEPARTAMENTOS -------------------- #

class DepartamentoList(ListView):
	model = Departamento
	template_name = 'clinicas/departamento_list.html'

class DepartamentoCreate(SuccessMessageMixin, CreateView):
	model = Departamento
	form_class = DepartamentoForm
	template_name = 'clinicas/departamento_form.html'
	success_url = reverse_lazy('clinicas:departamento_list')
	success_message = 'Departamento de %(nombre)s registrado correctamente'

class DepartamentoUpdate(SuccessMessageMixin, UpdateView):
	model = Departamento
	form_class = DepartamentoForm
	template_name = 'clinicas/departamento_form.html'
	success_url = reverse_lazy('clinicas:departamento_list')
	success_message = 'Departamento de %(nombre)s editado correctamente'

class DepartamentoDelete(SuccessMessageMixin, DeleteView):
	model = Departamento
	template_name = 'clinicas/departamento_delete.html'
	success_url = reverse_lazy('clinicas:departamento_list')
	success_message = 'Departamento de %(nombre)s eliminado correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(DepartamentoDelete, self).delete(request, *args, **kwargs)

# -------------------- CLÍNICAS -------------------- #

class ClinicaList(ListView):
	model = Clinica
	template_name = 'clinicas/clinica_list.html'

class ClinicaCreate(SuccessMessageMixin, CreateView):
	model = Clinica
	form_class = ClinicaForm
	template_name = 'clinicas/clinica_form.html'
	success_url = reverse_lazy('clinicas:clinica_list')
	success_message = 'Clínica %(nombre)s registrada correctamente'

class ClinicaUpdate(SuccessMessageMixin, UpdateView):
	model = Clinica
	form_class = ClinicaForm
	template_name = 'clinicas/clinica_form.html'
	success_url = reverse_lazy('clinicas:clinica_list')
	success_message = 'Clínica %(nombre)s editada correctamente'

class ClinicaDelete(SuccessMessageMixin, DeleteView):
	model = Clinica
	template_name = 'clinicas/clinica_delete.html'
	success_url = reverse_lazy('clinicas:clinica_list')
	success_message = 'Clinica %(nombre)s eliminada correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ClinicaDelete, self).delete(request, *args, **kwargs)
