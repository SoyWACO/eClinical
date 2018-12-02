from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.consultas.models import ColaEnfermeria
from apps.consultas.forms import ColaEnfermeriaForm
from apps.expediente.models import Expediente
from apps.clinicas.models import Clinica

# Create your views here.

# COLA DE ENFERMERIA #

class ColaEnfermeriaList(ListView):
	# model = ColaEnfermeria
	template_name = 'consultas/cola_enfermeria_list.html'

	def get_queryset(self):
		queryset = ColaEnfermeria.objects.filter(clinica=self.request.user.clinica.id)
		return queryset

class ColaEnfermeriaCreate(SuccessMessageMixin, CreateView):
	model = ColaEnfermeria
	form_class = ColaEnfermeriaForm
	template_name = 'consultas/cola_enfermeria_form.html'
	success_url = reverse_lazy('expediente:expediente_list')
	success_message = 'Expediente agregado a cola de enfermeria correctamente'

	'''def post(self, request, *args, **kwargs):
		#expediente_id = args['pk']
		expediente = Expediente.objects.get(id=self.kwargs['pk'])
		self.model.expediente = expediente
		self.save()
		return super(ColaEnfermeriaCreate, self).post(request, *args, **kwargs)
	'''

	'''def get_context_data(self, **kwargs):
		context = super(ColaEnfermeriaCreate, self).get_context_data(**kwargs)
		expediente = Expediente.objects.get(id=self.kwargs['pk'])
		self.model.expediente = expediente
		self.object.save()
		return context
	'''

	def get_initial(self):
		user = self.request.user
		diccionario = {
			'expediente':Expediente.objects.get(pk=self.kwargs["pk"]),
		}
		if user.clinica:
			diccionario['clinica'] = Clinica.objects.get(pk=user.clinica.id)
			pass
		return diccionario

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
