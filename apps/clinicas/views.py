from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.clinicas.models import Departamento
from apps.clinicas.forms import DepartamentoForm

# Create your views here.

class DepartamentoList(ListView):
	model = Departamento
	template_name = 'clinicas/departamento_list.html'

class DepartamentoCreate(CreateView):
	model = Departamento
	form_class = DepartamentoForm
	template_name = 'clinicas/departamento_form.html'
	success_url = reverse_lazy('clinicas:departamento_list')

class DepartamentoUpdate(UpdateView):
	model = Departamento
	form_class = DepartamentoForm
	template_name = 'clinicas/departamento_form.html'
	success_url = reverse_lazy('clinicas:departamento_list')

class DepartamentoDelete(DeleteView):
	model = Departamento
	template_name = 'clinicas/departamento_delete.html'
	success_url = reverse_lazy('clinicas:departamento_list')