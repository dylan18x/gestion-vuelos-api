from rest_framework import serializers
from vuelos.models import Escala  # Reemplaza 'vuelos' por el nombre real de tu app


class EscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escala
        fields = ['id', 'id_vuelo', 'aeropuerto_escala']
        read_only_fields = ['id']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Si existe la relación con el aeropuerto, anidamos los datos para Flutter
        if instance.aeropuerto_escala:
            representation['aeropuerto_escala'] = {
                # Usamos 'id_aeropuerto' que es tu primary_key personalizada en el modelo Aeropuerto
                'id': instance.aeropuerto_escala.id_aeropuerto,
                'nombre': instance.aeropuerto_escala.nombre,
                'ciudad': instance.aeropuerto_escala.ciudad,
                'pais': instance.aeropuerto_escala.pais,
                'codigo_iata': instance.aeropuerto_escala.codigo_iata,
            }
        return representation