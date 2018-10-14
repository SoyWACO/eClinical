from django.shortcuts import render
from django.urls import reverse_lazy
#from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.clinicas.models import Departamento
from apps.clinicas.forms import DepartamentoForm

# Create your views here.

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