from rest_framework import serializers
from vuelos.models import Ruta


class RutaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model  = Ruta
        fields = ['id', 'origen', 'destino']
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

    def validate(self, data):
        if data.get('origen') == data.get('destino'):
            raise serializers.ValidationError('El origen y destino no pueden ser el mismo aeropuerto.')
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.origen:
            representation['origen'] = {
                'id': instance.origen.id_aeropuerto,
                'nombre': instance.origen.nombre,
                'ciudad': instance.origen.ciudad,
                'codigo_iata': instance.origen.codigo_iata,
            }
            
        if instance.destino:
            representation['destino'] = {
                'id': instance.destino.id_aeropuerto,
                'nombre': instance.destino.nombre,
                'ciudad': instance.destino.ciudad,
                'codigo_iata': instance.destino.codigo_iata,
            }
            
        return representation