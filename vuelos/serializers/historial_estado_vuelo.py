from rest_framework import serializers
from vuelos.models import HistorialEstadoVuelo
from vuelos.serializers.estado_vuelo_serializer import EstadoVueloSerializer


class HistorialEstadoVueloSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        id_estado = EstadoVueloSerializer(read_only=True)
        model  = HistorialEstadoVuelo
        fields = ['id', 'fecha_cambio', 'observacion', 'id_vuelo', 'id_estado','image_url']
        read_only_fields = ['id', 'fecha_cambio']
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
        if instance.id_estado:
            representation['id_estado'] = {
                'id': instance.id_estado.id_estado,
                'nombre_estado': instance.id_estado.nombre_estado
            }
        return representation