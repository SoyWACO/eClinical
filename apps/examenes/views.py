from django.shortcuts import render


from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.examenes.models import PruebaEspecial, ExamenSangre
from apps.examenes.forms import PruebaEspecialForm, ExamenSangreForm
# Create your views here.

class PruebaEspecialList(ListView):
	model = PruebaEspecial
	template_name = 'examenes/prueba_especial_list.html'

class PruebaEspecialCreate(SuccessMessageMixin, CreateView):
	model = PruebaEspecial
	form_class = PruebaEspecialForm
	template_name = 'examenes/prueba_especial_form.html'
	success_url = reverse_lazy('examenes:prueba_especial_list')
	success_message = 'PruebaEspecial de %(codigo)s registrado correctamente'

class PruebaEspecialUpdate(SuccessMessageMixin, UpdateView):
	model = PruebaEspecial
	form_class = PruebaEspecialForm
	template_name = 'examenes/prueba_especial_form.html'
	success_url = reverse_lazy('examenes:prueba_especial_list')
	success_message = 'PruebaEspecial de %(codigo)s editado correctamente'

class PruebaEspecialDelete(SuccessMessageMixin, DeleteView):
	model = PruebaEspecial
	template_name = 'examenes/prueba_especial_delete.html'
	success_url = reverse_lazy('examenes:prueba_especial_list')
	success_message = 'PruebaEspecial de %(codigo)s eliminado correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(PruebaEspecialDelete, self).delete(request, *args, **kwargs)

#---------------------**********--------------------------****************************
class ExamenSangreList(ListView):
	model = ExamenSangre
	template_name = 'examenes/examen_sangre_list.html'

class ExamenSangreCreate(SuccessMessageMixin, CreateView):
	model = ExamenSangre
	form_class = ExamenSangreForm
	template_name = 'examenes/examen_sangre_form.html'
	success_url = reverse_lazy('examenes:examen_sangre_list')
	success_message = 'ExamenSangre de %(cod)s registrado correctamente'

class ExamenSangreUpdate(SuccessMessageMixin, UpdateView):
	model = ExamenSangre
	form_class = ExamenSangreForm
	template_name = 'examenes/examen_sangre_form.html'
	success_url = reverse_lazy('examenesexamen_sangre_list')
	success_message = 'ExamenSangre de %(cod)s editado correctamente'

class ExamenSangreDelete(SuccessMessageMixin, DeleteView):
	model = ExamenSangre
	template_name = 'examenes/examen_sangre_delete.html'
	success_url = reverse_lazy('examenes:examen_sangre_list')
	success_message = 'ExamenSangre de %(cod)s eliminado correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(PruebaEspecialDelete, self).delete(request, *args, **kwargs)

