from rest_framework import serializers
from vuelos.models import Vuelo


class VueloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vuelo
        fields = [
            'id',
            'codigo_vuelo',
            'fecha',
            'estado',
            'precio',
            'asientos_disponibles',
            'ruta',
            'id_avion'
        ]

        read_only_fields = ['id']


    def to_representation(self, instance):

        representation = super().to_representation(instance)


        # Avión + Aerolínea
        if instance.id_avion:
            representation['id_avion'] = {
                'id': instance.id_avion.id_avion,
                'modelo': instance.id_avion.modelo,
                'capacidad': instance.id_avion.capacidad,
                'matricula': instance.id_avion.matricula,

                'aerolinea': {
                    'id': (
                        instance.id_avion.id_aerolinea.id_aerolinea
                        if instance.id_avion.id_aerolinea
                        else None
                    ),

                    'nombre': (
                        instance.id_avion.id_aerolinea.nombre
                        if instance.id_avion.id_aerolinea
                        else None
                    ),

                    'pais': (
                        instance.id_avion.id_aerolinea.pais
                        if instance.id_avion.id_aerolinea
                        else None
                    )
                }
            }


        # Ruta
        if instance.ruta:
            representation['ruta'] = {

                'id': instance.ruta.id,

                'origen': {
                    'id': instance.ruta.origen.id_aeropuerto,
                    'nombre': instance.ruta.origen.nombre,
                    'ciudad': instance.ruta.origen.ciudad,
                    'pais': instance.ruta.origen.pais,
                    'image': (
                        instance.ruta.origen.image.url
                        if instance.ruta.origen.image
                        else None
                    )
                },

                'destino': {
                    'id': instance.ruta.destino.id_aeropuerto,
                    'nombre': instance.ruta.destino.nombre,
                    'ciudad': instance.ruta.destino.ciudad,
                    'pais': instance.ruta.destino.pais,
                    'image': (
                        instance.ruta.destino.image.url
                        if instance.ruta.destino.image
                        else None
                    )
                }
            }


        return representation



    def validate_codigo_vuelo(self, value):

        qs = Vuelo.objects.filter(
            codigo_vuelo__iexact=value
        )

        if self.instance:
            qs = qs.exclude(
                pk=self.instance.pk
            )

        if qs.exists():
            raise serializers.ValidationError(
                'Ya existe un vuelo con este código.'
            )

        return value.upper()