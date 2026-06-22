from rest_framework import serializers
from vuelos.models import Escala


class EscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Escala
        fields = ['id', 'id_vuelo', 'aeropuerto_escala']
        read_only_fields = ['id']