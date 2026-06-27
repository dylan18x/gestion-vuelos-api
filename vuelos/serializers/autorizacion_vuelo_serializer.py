from rest_framework import serializers
from vuelos.models.autorizacion_vuelo import AutorizacionVuelo

class AutorizacionVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorizacionVuelo
        fields = '__all__'