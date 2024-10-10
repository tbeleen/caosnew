from django.urls import path, include
from .views import *
from rest_framework import routers

#CONFIGURACION PARA EL API
router = routers.DefaultRouter()
router.register('tipoperiodistas', TipoPeriodistaViewset)
router.register('periodistas', PeriodistaViewset)
router.register('noticia', NoticiaViewset)
router.register('noticia', TipoNoticiaSerializers)

urlpatterns = [
    path('',index, name="index"),
    path('contact/',contact, name="contact"),
    path('periodista/', periodista , name="periodista"),
    path('periodista/add/', periodistaadd , name="periodistaadd"),
    path('periodista/update/<id>/', periodistaupdate , name="periodistaupdate"),
    path('periodista/delete/<id>/', periodistadelete , name="periodistadelete"),
    path('espectaculo/', espectaculo , name="espectaculo"),
    path('nacional/', nacional , name="nacional"),
    path('internacional/', internacional , name="internacional"),
    path('informatica/', informatica , name="informatica"),
    path('noticia/', noticia , name="noticia"),
    path('noticia/add/', noticiadd , name="noticiadd"),
    path('noticia/update/<id>/', noticiaupdate , name="noticiaupdate"),
    path('noticia/delete/<id>/', noticiadelete , name="noticiadelete"),
    path('register/',register,name="register"),
    path('solicitudes/',solicitudes,name="solicitudes"),
    path('solicitudupdate/<id>/',solicitudupdate,name="solicitudupdate"),
    path('solicitudadd/',solicitudadd,name="solicitudadd"),
    path('solicitudes/delete/<id>',solidelete,name="solidelete"),
    # ACOUNT LOCKED
    path('account_locked/', account_locked, name="account_locked"),
    #API
    path('api/', include(router.urls)),
    path('periodistasapi/', periodistasapi, name="periodistasapi"),
    path('servicios/', servicios, name="servicios"),
    path('dolarapi/', dolarapi, name="dolarapi"),
]