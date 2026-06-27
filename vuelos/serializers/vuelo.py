from rest_framework import serializers
from vuelos.models import Vuelo


class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Vuelo
        fields = ['id', 'codigo_vuelo', 'fecha', 'estado', 'id_avion']
        read_only_fields = ['id']

    def validate_codigo_vuelo(self, value):
        qs = Vuelo.objects.filter(codigo_vuelo__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('Ya existe un vuelo con este código.')
        return value.upper()