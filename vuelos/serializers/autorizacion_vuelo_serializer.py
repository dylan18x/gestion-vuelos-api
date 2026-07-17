from rest_framework import serializers
from vuelos.models.autorizacion_vuelo import AutorizacionVuelo


class AutorizacionVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorizacionVuelo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.id_vuelo:
            representation['id_vuelo'] = {
                'id': instance.id_vuelo.id,
                'codigo_vuelo': instance.id_vuelo.codigo_vuelo,
                'fecha': instance.id_vuelo.fecha,
                'estado': instance.id_vuelo.estado,
                'id_avion': {
                    'id': instance.id_vuelo.id_avion.id_avion,
                    'modelo': instance.id_vuelo.id_avion.modelo,
                    'capacidad': instance.id_vuelo.id_avion.capacidad,
                    'matricula': instance.id_vuelo.id_avion.matricula,
                    'aerolinea': {
                        'id': (
                            instance.id_vuelo.id_avion.id_aerolinea.id_aerolinea
                            if instance.id_vuelo.id_avion.id_aerolinea
                            else None
                        ),
                        'nombre': (
                            instance.id_vuelo.id_avion.id_aerolinea.nombre
                            if instance.id_vuelo.id_avion.id_aerolinea
                            else None
                        ),
                        'pais': (
                            instance.id_vuelo.id_avion.id_aerolinea.pais
                            if instance.id_vuelo.id_avion.id_aerolinea
                            else None
                        ),
                    }
                }
            }

        return representation