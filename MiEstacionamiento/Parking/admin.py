from django.contrib import admin
from .models import Place,Vehiculo,Usuario


admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(Place)