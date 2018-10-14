from django.urls import path
from apps.usuarios.views import GroupList, GroupCreate, GroupUpdate, GroupDelete

app_name = 'usuarios'

urlpatterns = [
	path('roles/', GroupList.as_view(), name='rol_list'),
	path('roles/add/', GroupCreate.as_view(), name='rol_create'),
	path('roles/<pk>/change/', GroupUpdate.as_view(), name='rol_update'),
	path('roles/<pk>/delete/', GroupDelete.as_view(), name='rol_delete'),
]