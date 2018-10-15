from django.urls import path
from apps.usuarios.views import GroupList, GroupCreate, GroupUpdate, GroupDelete, \
	UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDelete

app_name = 'usuarios'

urlpatterns = [

	# Roles de Usuario
	path('roles/', GroupList.as_view(), name='rol_list'),
	path('roles/add/', GroupCreate.as_view(), name='rol_create'),
	path('roles/<pk>/change/', GroupUpdate.as_view(), name='rol_update'),
	path('roles/<pk>/delete/', GroupDelete.as_view(), name='rol_delete'),

	# Usuarios
	path('usuarios/', UsuarioList.as_view(), name='usuario_list'),
	path('usuarios/add/', UsuarioCreate.as_view(), name='usuario_create'),
	path('usuarios/<pk>/change/', UsuarioUpdate.as_view(), name='usuario_update'),
	path('usuarios/<pk>/delete/', UsuarioDelete.as_view(), name='usuario_delete'),
]