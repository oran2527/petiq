from rest_framework import serializers
from .models import Countries
from .models import States
from .models import Cities
from .models import Owners

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = "__all__"

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = "__all__"

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = "__all__"

class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owners
        fields = "__all__"