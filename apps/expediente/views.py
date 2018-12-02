from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.expediente.models import Expediente,SignoVital
from apps.expediente.forms import ExpedienteForm, SignoVitalForm


# Create your views here.

# SIGNOS VITALES #

class SignoVitalList(ListView):
	model = SignoVital
	template_name = 'expediente/signo_vital_list.html'

class SignoVitalCreate(SuccessMessageMixin, CreateView):
	model = SignoVital
	form_class = SignoVitalForm
	template_name = 'expediente/signo_vital_form.html'
	success_url = reverse_lazy('expediente:signo_vital_list')
	success_message = 'Signos vitales registrados correctamente'

class SignoVitalUpdate(SuccessMessageMixin, UpdateView):
	model = SignoVital
	form_class = SignoVitalForm
	template_name = 'expediente/signo_vital_form.html'
	success_url = reverse_lazy('expediente:signo_vital_list')
	success_message = 'Signos vitales editados correctamente'

class SignoVitalDelete(SuccessMessageMixin, DeleteView):
	model = SignoVital
	template_name = 'expediente/signo_vital_delete.html'
	success_url = reverse_lazy('expediente:signo_vital_list')
	success_message = 'Signos vitales eliminados correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(SignoVitalDelete, self).delete(request, *args, **kwargs)

#---------------------------Expediente--------------------------------- #
class ExpedienteList(ListView):
	model = Expediente
	template_name = 'expediente/expediente_list.html'

class ExpedienteCreate(SuccessMessageMixin, CreateView):
	model = Expediente
	form_class = ExpedienteForm
	template_name = 'expediente/expediente_form.html'
	success_url = reverse_lazy('expediente:expediente_list')
	success_message = 'Expediente registrados correctamente'

class ExpedienteUpdate(SuccessMessageMixin, UpdateView):
	model = Expediente
	form_class = ExpedienteForm
	template_name = 'expediente/expediente_form.html'
	success_url = reverse_lazy('expediente:expediente_list')
	success_message = 'Expediente editados correctamente'

class ExpedienteDelete(SuccessMessageMixin, DeleteView):
	model = Expediente
	template_name = 'expediente/expediente_delete.html'
	success_url = reverse_lazy('expediente:expediente_list')
	success_message = 'Expediente eliminados correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ExpedienteDelete, self).delete(request, *args, **kwargs)


# EXPEDIENTES #

class ExpedienteView(TemplateView):

    template_name = "expediente/expediente_view.html"

    '''Para los datos
    def get_context_data(self, **kwargs):
    	article = get_object_or_404(Article, pk=kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context'''
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expediente'] = Expediente.objects.get(pk=kwargs['pk'])
        return context
