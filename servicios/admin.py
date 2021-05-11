from django.contrib import admin
# aca importamos la clase servicio del modelo
from .models import servicio

# Register your models here.
class servicioAdmin(admin.ModelAdmin):
    #vamos a mostrar campos update y delet
    readonly_fields = ("created","updated")
admin.site.register(servicio,servicioAdmin)