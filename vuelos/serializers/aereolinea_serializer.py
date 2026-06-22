# serializers.py

from rest_framework import serializers
from ..models import Aerolinea

class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aerolinea
        fields = '__all__'