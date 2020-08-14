from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Countries
from .models import States
from .models import Cities
from .models import Owners
from .serializers import CountriesSerializer
from .serializers import StatesSerializer
from .serializers import CitiesSerializer
from .serializers import OwnersSerializer

class CountriesAPIView(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

class StatesAPIView(generics.ListCreateAPIView):
    queryset = States.objects.all()
    serializer_class = StatesSerializer

class CitiesAPIView(generics.ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

class OwnersAPIView(generics.ListCreateAPIView):
    queryset = Owners.objects.all()
    serializer_class = OwnersSerializer