# vuelos/serializers/estado_vuelo_serializer.py
from rest_framework import serializers
from ..models import EstadoVuelo

class EstadoVueloSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = EstadoVuelo
        fields = '__all__'