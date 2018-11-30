from django.urls import path
from apps.examenes.views import PruebaEspecialList, PruebaEspecialCreate, PruebaEspecialUpdate, PruebaEspecialDelete,\
       ExamenSangreList, ExamenSangreCreate, ExamenSangreUpdate, ExamenSangreDelete,\
       ExamenOrinaList, ExamenOrinaCreate, ExamenOrinaUpdate, ExamenOrinaDelete,\
       ExamenHecesList, ExamenHecesCreate, ExamenHecesUpdate, ExamenHecesDelete




app_name = 'examenes'

urlpatterns = [

	# Signos Vitales
	path('prueba_especial/', PruebaEspecialList.as_view(), name='prueba_especial_list'),
	path('prueba_especial/add/', PruebaEspecialCreate.as_view(), name='prueba_especial_create'),
	path('prueba_especial/<pk>/change/', PruebaEspecialUpdate.as_view(), name='prueba_especial_update'),
	path('prueba_especial/<pk>/delete/', PruebaEspecialDelete.as_view(), name='prueba_especial_delete'),
    #examen de sanggre
    path('examen_sangre/', ExamenSangreList.as_view(), name='examen_sangre_list'),
	path('examen_sangre/add/', ExamenSangreCreate.as_view(), name='examen_sangre_create'),
	path('examen_sangre/<pk>/change/', ExamenSangreUpdate.as_view(), name='examen_sangre_update'),
	path('/<pk>/delete/',ExamenSangreDelete.as_view(), name='examen_sangre_delete'),

	#examen de orina
    path('examen_orina/', ExamenOrinaList.as_view(), name='examen_orina_list'),
	path('examen_orina/add/', ExamenOrinaCreate.as_view(), name='examen_orina_create'),
	path('examen_orina/<pk>/change/', ExamenOrinaUpdate.as_view(), name='examen_orina_update'),
	path('/<pk>/delete/',ExamenOrinaDelete.as_view(), name='examen_orina_delete'),

   #examen de heces
    path('examen_heces/', ExamenHecesList.as_view(), name='examen_heces_list'),
	path('examen_heces/add/', ExamenHecesCreate.as_view(), name='examen_heces_create'),
	path('examen_heces/<pk>/change/', ExamenHecesUpdate.as_view(), name='examen_heces_update'),
	path('/<pk>/delete/',ExamenHecesDelete.as_view(), name='examen_heces_delete'),

]