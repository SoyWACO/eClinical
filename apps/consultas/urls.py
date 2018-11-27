from django.urls import path
from apps.consultas.views import ColaEnfermeriaList, ColaEnfermeriaCreate, ColaEnfermeriaUpdate, ColaEnfermeriaDelete

app_name = 'consultas'

urlpatterns = [

	# Cola Enfermeria
	path('cola_enfermeria/', ColaEnfermeriaList.as_view(), name='cola_enfermeria_list'),
	path('cola_enfermeria/<pk>/add/', ColaEnfermeriaCreate.as_view(), name='cola_enfermeria_create'),
	path('cola_enfermeria/<pk>/change/', ColaEnfermeriaUpdate.as_view(), name='cola_enfermeria_update'),
	path('cola_enfermeria/<pk>/delete/', ColaEnfermeriaDelete.as_view(), name='cola_enfermeria_delete'),
]