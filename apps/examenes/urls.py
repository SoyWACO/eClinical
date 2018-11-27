from django.urls import path
from apps.examenes.views import PruebaEspecialList, PruebaEspecialCreate, PruebaEspecialUpdate, PruebaEspecialDelete


app_name = 'examenes'

urlpatterns = [

	# Signos Vitales
	path('prueba_especial/', PruebaEspecialList.as_view(), name='prueba_especial_list'),
	path('prueba_especial/add/', PruebaEspecialCreate.as_view(), name='prueba_especial_create'),
	path('prueba_especial/<pk>/change/', PruebaEspecialUpdate.as_view(), name='prueba_especial_update'),
	path('prueba_especial/<pk>/delete/', PruebaEspecialDelete.as_view(), name='prueba_especial_delete'),
]