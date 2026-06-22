from rest_framework import serializers
from vuelos.models import ControlTrafico


class ControlTraficoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ControlTrafico
        fields = ['id', 'autorizacion', 'hora', 'id_vuelo']
        read_only_fields = ['id']