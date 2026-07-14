from rest_framework import serializers
from vuelos.models.autorizacion_vuelo import AutorizacionVuelo

class AutorizacionVueloSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = AutorizacionVuelo
        fields = '__all__'