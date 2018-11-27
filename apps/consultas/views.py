from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.consultas.models import ColaEnfermeria
from apps.consultas.forms import ColaEnfermeriaForm

# Create your views here.

# COLA DE ENFERMERIA #

class ColaEnfermeriaList(ListView):
	model = ColaEnfermeria
	template_name = 'consultas/cola_enfermeria_list.html'

class ColaEnfermeriaCreate(SuccessMessageMixin, CreateView):
	model = ColaEnfermeria
	form_class = ColaEnfermeriaForm
	template_name = 'consultas/cola_enfermeria_form.html'
	success_url = reverse_lazy('consultas:cola_enfermeria_list')
	success_message = 'Expediente agregado a cola de enfermeria correctamente'

class ColaEnfermeriaUpdate(SuccessMessageMixin, UpdateView):
	model = ColaEnfermeria
	form_class = ColaEnfermeriaForm
	template_name = 'consultas/cola_enfermeria_form.html'
	success_url = reverse_lazy('consultas:cola_enfermeria_list')
	success_message = 'Registro editado correctamente'

class ColaEnfermeriaDelete(SuccessMessageMixin, DeleteView):
	model = ColaEnfermeria
	template_name = 'consultas/cola_enfermeria_delete.html'
	success_url = reverse_lazy('consultas:cola_enfermeria_list')
	success_message = 'Expediente eliminado de cola de enfermeria correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ColaEnfermeriaDelete, self).delete(request, *args, **kwargs)
