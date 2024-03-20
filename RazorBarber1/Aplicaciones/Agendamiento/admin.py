from django.contrib import admin
from .models import Rol, Cliente, Barbero  
# Register your models here.
admin.site.register(Rol)
admin.site.register(Cliente)
admin.site.register(Barbero)