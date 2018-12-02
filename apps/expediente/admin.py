from django.contrib import admin
from apps.expediente.models import SignoVital, Expediente

# Register your models here.

admin.site.register(SignoVital)
admin.site.register(Expediente)