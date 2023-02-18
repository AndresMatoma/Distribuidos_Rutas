from rest_framework import serializers
from app.models import *

class BusSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Bus
        fields = ('matricula','marca','modelo','capacidad')

class ParaderoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Paradero
        fields = ('latitud','longitud','nombre')

class HoraSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Horario
        fields = ('horario',)

class RutaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ruta
        fields = ('bus','paradero','hora')
    def to_representation(self, instance):
        return {
            'bus': instance.bus.matricula,
            'longitud': instance.paradero.longitud,
            'latitud': instance.paradero.latitud,
            'ubicacion': instance.paradero.nombre,
            'hora': instance.hora.horario,

        }