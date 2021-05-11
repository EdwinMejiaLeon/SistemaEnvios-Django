from django.urls import path
#vamos a importar las urls
from  servicios import views
#estas librerias son para static
from django.conf import settings
from django.conf.urls.static import static
#vamos a importar la configuracion de media que se usa en la administracion
from django.conf import settings


urlpatterns = [
    path('', views.servicios, name="Servicios"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)