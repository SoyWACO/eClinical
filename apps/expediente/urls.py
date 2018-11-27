from django.urls import path
from apps.expediente.views import SignoVitalList, SignoVitalCreate, SignoVitalUpdate, SignoVitalDelete, \
	ExpedienteList, ExpedienteCreate, ExpedienteUpdate, ExpedienteDelete,ExpedienteView


app_name = 'expediente'

urlpatterns = [

	# Signos Vitales
	path('signo_vitales/', SignoVitalList.as_view(), name='signo_vital_list'),
	path('signo_vitales/add/', SignoVitalCreate.as_view(), name='signo_vital_create'),
	path('signo_vitales/<pk>/change/', SignoVitalUpdate.as_view(), name='signo_vital_update'),
	path('signo_vitales/<pk>/delete/', SignoVitalDelete.as_view(), name='signo_vital_delete'),


	#expediente
	path('expediente/', ExpedienteList.as_view(), name='expediente_list'),
	path('expediente/add/', ExpedienteCreate.as_view(), name='expediente_create'),
	path('expediente/<pk>/change/', ExpedienteUpdate.as_view(), name='expediente_update'),
	path('expediente/<pk>/delete/', ExpedienteDelete.as_view(), name='expediente_delete'),
	# EXPEDIENTE #
	# Falta agregar id del expediente
	path('<pk>/view/', ExpedienteView.as_view(), name='expediente_view'),

]