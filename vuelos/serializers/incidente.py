from rest_framework import serializers
from vuelos.models import Incidente


class IncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Incidente
        fields = ['id', 'descripcion', 'fecha', 'id_vuelo']
        read_only_fields = ['id']