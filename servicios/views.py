from django.shortcuts import render
#vamos a importar los servicios  puestos en la administracion 
from servicios.models import servicio


def servicios (request):
    #con esto importa los servicios contruidos
    servicios = servicio.objects.all()
    return render(request, "servicios.html", {"servicios":servicios})