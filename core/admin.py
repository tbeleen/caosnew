from django.contrib import admin
from .models import *
from admin_confirm import AdminConfirmMixin
from django.contrib.admin import ModelAdmin

class PeriodistaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['rut', 'nombre','edad','direccion','telefono','fecha_contrato','genero','TipoPeriodista','imagen']
    
class TipoPeriodistaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['descripcion']
    
class TipoNoticiaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['descripcion']
    
class NoticiaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['periodista', 'TipoNoticia','titulo','descripcion','fecha','imagen','estado','motivo']

# Register your models here.

admin.site.register(TipoPeriodista, TipoPeriodistaModelAdmin)
admin.site.register(Periodista, PeriodistaModelAdmin)
admin.site.register(TipoNoticia, TipoNoticiaModelAdmin)
admin.site.register(Noticia, NoticiaModelAdmin)