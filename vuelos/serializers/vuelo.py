from rest_framework import serializers
from vuelos.models import Vuelo


class VueloSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model  = Vuelo
        fields = ['id', 'codigo_vuelo', 'fecha', 'estado', 'id_avion','image_url']
        read_only_fields = ['id']
        extra_kwargs = {
            'image': {
                'required': False,
                'allow_null': True,
            }
        }

    def get_image_url(self, obj):
        request = self.context.get('request')

        if obj.image:
            return (
                request.build_absolute_uri(obj.image.url)
                if request
                else obj.image.url
            )

        return None

    def validate_image(self, value):
        max_size = 2 * 1024 * 1024  # 2 MB
        valid_types = [
            'image/jpeg',
            'image/png',
            'image/webp',
        ]

        if value and value.size > max_size:
            raise serializers.ValidationError(
                'La imagen no puede superar los 2 MB.'
            )

        if value and value.content_type not in valid_types:
            raise serializers.ValidationError(
                'Solo se permiten imágenes JPEG, PNG y WebP.'
            )

        return value
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.id_avion:
            representation['id_avion'] = {
                'id': instance.id_avion.id_avion,
                'modelo': instance.id_avion.modelo,
                'capacidad':instance.id_avion.capacidad,
                'matricula': instance.id_avion.matricula,
                'aerolinea': {
                    'id': instance.id_avion.id_aerolinea.id_aerolinea if instance.id_avion.id_aerolinea else None,
                    'nombre': instance.id_avion.id_aerolinea.nombre if instance.id_avion.id_aerolinea else None, 
                    'pais': instance.id_avion.id_aerolinea.pais if instance.id_avion.id_aerolinea else None
                } 
            }
        return representation

    def validate_codigo_vuelo(self, value):
        qs = Vuelo.objects.filter(codigo_vuelo__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('Ya existe un vuelo con este código.')
        return value.upper()