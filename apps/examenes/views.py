from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.examenes.models import PruebaEspecial, ExamenSangre, ExamenOrina, ExamenHeces, ExamenFisico
from apps.examenes.forms import PruebaEspecialForm, ExamenSangreForm, ExamenOrinaForm, ExamenHecesForm, ExamenFisicoForm

# Create your views here.

class PruebaEspecialList(ListView):
	model = PruebaEspecial
	template_name = 'examenes/prueba_especial_list.html'

class PruebaEspecialCreate(SuccessMessageMixin, CreateView):
	model = PruebaEspecial
	form_class = PruebaEspecialForm
	template_name = 'examenes/prueba_especial_form.html'
	success_url = reverse_lazy('examenes:prueba_especial_list')
	success_message = 'Prueba Especial de registrada correctamente'

class PruebaEspecialUpdate(SuccessMessageMixin, UpdateView):
	model = PruebaEspecial
	form_class = PruebaEspecialForm
	template_name = 'examenes/prueba_especial_form.html'
	success_url = reverse_lazy('examenes:prueba_especial_list')
	success_message = 'Prueba Especial editada correctamente'

class PruebaEspecialDelete(SuccessMessageMixin, DeleteView):
	model = PruebaEspecial
	template_name = 'examenes/prueba_especial_delete.html'
	success_url = reverse_lazy('examenes:prueba_especial_list')
	success_message = 'Prueba Especial eliminada correctamente'

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
	success_message = 'Examen de Sangre registrado correctamente'

class ExamenSangreUpdate(SuccessMessageMixin, UpdateView):
	model = ExamenSangre
	form_class = ExamenSangreForm
	template_name = 'examenes/examen_sangre_form.html'
	success_url = reverse_lazy('examenes:examen_sangre_list')
	success_message = 'Examen de Sangre editado correctamente'

class ExamenSangreDelete(SuccessMessageMixin, DeleteView):
	model = ExamenSangre
	template_name = 'examenes/examen_sangre_delete.html'
	success_url = reverse_lazy('examenes:examen_sangre_list')
	success_message = 'Examen de Sangre eliminado correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ExamenSangreDelete, self).delete(request, *args, **kwargs)

#________________________________________________________________________________

class ExamenOrinaList(ListView):
	model = ExamenOrina
	template_name = 'examenes/examen_orina_list.html'

class ExamenOrinaCreate(SuccessMessageMixin, CreateView):
	model = ExamenOrina
	form_class = ExamenOrinaForm
	template_name = 'examenes/examen_orina_form.html'
	success_url = reverse_lazy('examenes:examen_orina_list')
	success_message = 'Examen de Orina registrado correctamente'

class ExamenOrinaUpdate(SuccessMessageMixin, UpdateView):
	model = ExamenOrina
	form_class = ExamenOrinaForm
	template_name = 'examenes/examen_orina_form.html'
	success_url = reverse_lazy('examenes:examen_orina_list')
	success_message = 'Examen de Orina editado correctamente'

class ExamenOrinaDelete(SuccessMessageMixin, DeleteView):
	model = ExamenOrina
	template_name = 'examenes/examen_orina_delete.html'
	success_url = reverse_lazy('examenes:examen_orina_list')
	success_message = 'Examen de Orina eliminado correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ExamenOrinaDelete, self).delete(request, *args, **kwargs)

#____________________________________________________________________________

class ExamenHecesList(ListView):
	model = ExamenHeces
	template_name = 'examenes/examen_heces_list.html'

class ExamenHecesCreate(SuccessMessageMixin, CreateView):
	model = ExamenHeces
	form_class = ExamenHecesForm
	template_name = 'examenes/examen_heces_form.html'
	success_url = reverse_lazy('examenes:examen_heces_list')
	success_message = 'Examen de Heces registrado correctamente'

class ExamenHecesUpdate(SuccessMessageMixin, UpdateView):
	model = ExamenHeces
	form_class = ExamenHecesForm
	template_name = 'examenes/examen_heces_form.html'
	success_url = reverse_lazy('examenes:examen_heces_list')
	success_message = 'Examen de Heces editado correctamente'

class ExamenHecesDelete(SuccessMessageMixin, DeleteView):
	model = ExamenHeces
	template_name = 'examenes/examen_heces_delete.html'
	success_url = reverse_lazy('examenes:examen_heces_list')
	success_message = 'Examen de Heces eliminado correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ExamenHecesDelete, self).delete(request, *args, **kwargs)

#____________________________________________________________________________

class ExamenFisicoList(ListView):
	model = ExamenFisico
	template_name = 'examenes/examen_fisico_list.html'

class ExamenFisicoCreate(SuccessMessageMixin, CreateView):
	model = ExamenFisico
	form_class = ExamenFisicoForm
	template_name = 'examenes/examen_fisico_form.html'
	success_url = reverse_lazy('examenes:examen_fisico_list')
	success_message = 'Examen Fisico registrado correctamente'

class ExamenFisicoUpdate(SuccessMessageMixin, UpdateView):
	model = ExamenFisico
	form_class = ExamenFisicoForm
	template_name = 'examenes/examen_fisico_form.html'
	success_url = reverse_lazy('examenes:examen_fisico_list')
	success_message = 'Examen Fisico editado correctamente'

class ExamenFisicoDelete(SuccessMessageMixin, DeleteView):
	model = ExamenFisico
	template_name = 'examenes/examen_fisico_delete.html'
	success_url = reverse_lazy('examenes:examen_fisico_list')
	success_message = 'Examen Fisico eliminado correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ExamenFisicoDelete, self).delete(request, *args, **kwargs)