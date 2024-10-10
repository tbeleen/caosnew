from rest_framework import serializers
from .models import *

class TipoPeriodistaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoPeriodista
        fields = '__all__'

class PeriodistaSerializers(serializers.ModelSerializer):
    TipoPeriodista = TipoPeriodistaSerializers(read_only=True)
    class Meta:
        model = Periodista
        fields = '__all__'

class TipoNoticiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoNoticia
        fields = '__all__'        

class NoticiaSerializers(serializers.ModelSerializer):
    TipoNoticia = TipoNoticiaSerializers(read_only=True)
    class Meta:
        model = Noticia
        fields = '__all__'