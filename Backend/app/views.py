from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.serializers import * 
# Create your views here.
@api_view(['GET',])
def bus (request):
    Permission_class=(IsAuthenticated,)
    if request.method =='GET':
        bus=Bus.objects.all()
        bus_serializers=BusSerializer(bus,many=True)
        return Response(bus_serializers.data)

@api_view(['GET',])
def hora (request):
    Permission_class=(IsAuthenticated,)
    if request.method =='GET':
        hora=Horario.objects.all()
        hora_serializers=HoraSerializer(hora,many=True)
        return Response(hora_serializers.data)

@api_view(['GET',])
def ruta (request):
    Permission_class=(IsAuthenticated,)
    if request.method =='GET':
        ruta=Ruta.objects.all()
        ruta_serializers=RutaSerializer(ruta,many=True)
        return Response(ruta_serializers.data)

@api_view(['GET',])
def paradero (request):
    Permission_class=(IsAuthenticated,)
    if request.method =='GET':
        paradero=Paradero.objects.all()
        paradero_serializers=ParaderoSerializer(paradero,many=True)
        return Response(paradero_serializers.data)