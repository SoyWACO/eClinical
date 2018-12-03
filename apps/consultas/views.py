from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.consultas.models import ColaEnfermeria, ColaConsulta, ConsultaMedica
from apps.consultas.forms import ColaEnfermeriaForm, ColaConsultaForm, ConsultaMedicaForm
from apps.expediente.models import Expediente
from apps.clinicas.models import Clinica, Departamento
from apps.usuarios.models import Usuario

# Create your views here.

# ------------------ COLA DE ENFERMERIA ------------------ #

class ColaEnfermeriaList(ListView):
	template_name = 'consultas/cola_enfermeria_list.html'

	def get_queryset(self):
		user = self.request.user
		if user.clinica:
			queryset = ColaEnfermeria.objects.filter(clinica=user.clinica.id)
			pass
		else:
			queryset = ColaEnfermeria.objects.all()
			pass
		return queryset

class ColaEnfermeriaCreate(SuccessMessageMixin, CreateView):
	model = ColaEnfermeria
	form_class = ColaEnfermeriaForm
	template_name = 'consultas/cola_enfermeria_form.html'
	success_url = reverse_lazy('expediente:expediente_list')
	success_message = 'Expediente agregado a cola de enfermería correctamente'

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
	success_message = 'Expediente eliminado de cola de enfermería correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ColaEnfermeriaDelete, self).delete(request, *args, **kwargs)

# --------------- COLA DE CONSULTA MEDICA ---------------- #

class ColaConsultaList(ListView):
	template_name = 'consultas/cola_consulta_list.html'

	def get_queryset(self):
		user = self.request.user
		if user.clinica:
			queryset = ColaConsulta.objects.filter(clinica=user.clinica.id, usuario=user.id)
			pass
		else:
			queryset = ColaConsulta.objects.all()
			pass
		return queryset

class ColaConsultaCreate(SuccessMessageMixin, CreateView):
	model = ColaConsulta
	form_class = ColaConsultaForm
	template_name = 'consultas/cola_consulta_form.html'
	success_url = reverse_lazy('consultas:cola_enfermeria_list')
	success_message = 'Expediente agregado a cola de consulta correctamente'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['paciente'] = self.kwargs["pk"]
		return context

	def get_initial(self):
		user = self.request.user
		diccionario = {
			'expediente':Expediente.objects.get(pk=self.kwargs["pk"]),
		}
		if user.clinica:
			diccionario['clinica'] = Clinica.objects.get(pk=user.clinica.id)
			#departamento = Departamento.objects.get(pk=self.kwargs["departamento"])
			#diccionario['usuario'] = departamento.usuario_set.all()
			pass
		return diccionario

	'''def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'usuario_id':
			departamento = Departamento.objects.get(pk=self.kwargs["departamento"])
			kwargs['departamento'] = departamento.usuario_set.all()
			return super(ColaConsultaCreate, self).formfield_for_foreignkey(db_field, request, **kwargs)'''

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs["departamento"] = self.kwargs["departamento"]
		return kwargs

class ColaConsultaUpdate(SuccessMessageMixin, UpdateView):
	model = ColaConsulta
	form_class = ColaConsultaForm
	template_name = 'consultas/cola_consulta_form.html'
	success_url = reverse_lazy('consultas:cola_consulta_list')
	success_message = 'Registro editado correctamente'

class ColaConsultaDelete(SuccessMessageMixin, DeleteView):
	model = ColaConsulta
	template_name = 'consultas/cola_consulta_delete.html'
	success_url = reverse_lazy('consultas:cola_consulta_list')
	success_message = 'Expediente eliminado de cola de consulta correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ColaConsultaDelete, self).delete(request, *args, **kwargs)

class ColaConsultaDepartamento(TemplateView):

	template_name = "consultas/cola_consulta_departamento.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = self.request.user
		if user.clinica:
			clinica = Clinica.objects.get(pk=user.clinica.id)
			context['departamentos'] = clinica.departamentos.all()
			pass
		else:
			context['departamentos'] = Departamento.objects.all()
			pass
		context['paciente'] = Expediente.objects.get(pk=self.kwargs["pk"])
		return context

# -------------------- CONSULTA MEDICA ------------------- #

class ConsultaMedicaList(ListView):
	template_name = 'consultas/consulta_medica_list.html'

	def get_queryset(self):
		user = self.request.user
		if user.clinica:
			queryset = ConsultaMedica.objects.filter(clinica=user.clinica.id)
			pass
		else:
			queryset = ConsultaMedica.objects.all()
			pass
		return queryset

class ConsultaMedicaCreate(SuccessMessageMixin, CreateView):
	model = ConsultaMedica
	form_class = ConsultaMedicaForm
	template_name = 'consultas/consulta_medica_form.html'
	success_url = reverse_lazy('consultas:cola_consulta_list')
	success_message = 'Consulta médica registrada correctamente'

	def get_initial(self):
		user = self.request.user
		diccionario = {
			'expediente':Expediente.objects.get(pk=self.kwargs["pk"]),
			'usuario':Usuario.objects.get(pk=user.id),
		}
		return diccionario

class ConsultaMedicaUpdate(SuccessMessageMixin, UpdateView):
	model = ConsultaMedica
	form_class = ConsultaMedicaForm
	template_name = 'consultas/consulta_medica_form.html'
	success_url = reverse_lazy('consultas:cola_consulta_list')
	success_message = 'Registro editado correctamente'

class ConsultaMedicaDelete(SuccessMessageMixin, DeleteView):
	model = ConsultaMedica
	template_name = 'consultas/consulta_medica_delete.html'
	success_url = reverse_lazy('consultas:cola_consulta_list')
	success_message = 'Consulta médica eliminada correctamente'

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(ConsultaMedicaDelete, self).delete(request, *args, **kwargs)