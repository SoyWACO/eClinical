from django.urls import path
from apps.examenes.views import PruebaEspecialList, PruebaEspecialCreate, PruebaEspecialUpdate, PruebaEspecialDelete,\
       ExamenSangreList, ExamenSangreCreate, ExamenSangreUpdate, ExamenSangreDelete




app_name = 'examenes'

urlpatterns = [

	# Signos Vitales
	path('prueba_especial/', PruebaEspecialList.as_view(), name='prueba_especial_list'),
	path('prueba_especial/add/', PruebaEspecialCreate.as_view(), name='prueba_especial_create'),
	path('prueba_especial/<pk>/change/', PruebaEspecialUpdate.as_view(), name='prueba_especial_update'),
	path('prueba_especial/<pk>/delete/', PruebaEspecialDelete.as_view(), name='prueba_especial_delete'),

    path('examen_sangre/', ExamenSangreList.as_view(), name='examen_sangre_list'),
	path('examen_sangre/add/', ExamenSangreCreate.as_view(), name='examen_sangre_create'),
	path('examen_sangre/<pk>/change/', ExamenSangreUpdate.as_view(), name='examen_sangre_update'),
	path('/<pk>/delete/',ExamenSangreDelete.as_view(), name='examen_sangre_delete'),

]