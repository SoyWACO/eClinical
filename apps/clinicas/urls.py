from django.urls import path
from apps.clinicas.views import DepartamentoList, DepartamentoCreate, DepartamentoUpdate, DepartamentoDelete

app_name = 'clinicas'

urlpatterns = [
	path('departamentos/', DepartamentoList.as_view(), name='departamento_list'),
	path('departamentos/add/', DepartamentoCreate.as_view(), name='departamento_create'),
	path('departamentos/<pk>/change/', DepartamentoUpdate.as_view(), name='departamento_update'),
	path('departamentos/<pk>/delete/', DepartamentoDelete.as_view(), name='departamento_delete'),
]