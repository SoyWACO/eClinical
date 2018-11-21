from django.urls import path
from apps.expediente.views import SignoVitalList, SignoVitalCreate, SignoVitalUpdate, SignoVitalDelete, \
	ExpedienteView

app_name = 'expediente'

urlpatterns = [

	# Signos Vitales
	path('signo_vitales/', SignoVitalList.as_view(), name='signo_vital_list'),
	path('signo_vitales/add/', SignoVitalCreate.as_view(), name='signo_vital_create'),
	path('signo_vitales/<pk>/change/', SignoVitalUpdate.as_view(), name='signo_vital_update'),
	path('signo_vitales/<pk>/delete/', SignoVitalDelete.as_view(), name='signo_vital_delete'),

	# EXPEDIENTE #
	# Falta agregar id del expediente
	path('view/', ExpedienteView.as_view(), name='expediente_view'),
]