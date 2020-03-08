from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import EnergySerializer
from rest_framework.response import Response

from .models import house

# Create your views here.

# fetches 
@api_view(['get'])
def fetch_neighbourhood(request):
    house_energy_use = house.objects.all()
    #serialize
    serializer = EnergySerializer(house_energy_use, many=True)
    #return Response using rest_framework's response
    return Response(serializer.data)

@api_view(['get'])
def fetch_rankings(request):
    houses = house.objects.all().filter(logged_date="2020-02-20").order_by('-heat_use')
    serializer = EnergySerializer(houses, many=True)
    return Response(serializer.data)