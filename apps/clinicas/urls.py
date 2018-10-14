from django.urls import path
from apps.clinicas.views import DepartamentoList, DepartamentoCreate, DepartamentoUpdate, DepartamentoDelete, \
		ClinicaList, ClinicaCreate, ClinicaUpdate, ClinicaDelete

app_name = 'clinicas'

urlpatterns = [

	# Departamentos
	path('departamentos/', DepartamentoList.as_view(), name='departamento_list'),
	path('departamentos/add/', DepartamentoCreate.as_view(), name='departamento_create'),
	path('departamentos/<pk>/change/', DepartamentoUpdate.as_view(), name='departamento_update'),
	path('departamentos/<pk>/delete/', DepartamentoDelete.as_view(), name='departamento_delete'),

	# Clínicas
	path('clinicas/', ClinicaList.as_view(), name='clinica_list'),
	path('clinicas/add/', ClinicaCreate.as_view(), name='clinica_create'),
	path('clinicas/<pk>/change/', ClinicaUpdate.as_view(), name='clinica_update'),
	path('clinicas/<pk>/delete/', ClinicaDelete.as_view(), name='clinica_delete'),
]