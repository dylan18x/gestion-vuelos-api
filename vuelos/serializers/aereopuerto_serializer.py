# serializers.py

from rest_framework import serializers
from ..models import Aeropuerto

class AeropuertoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Aeropuerto
        fields = '__all__'