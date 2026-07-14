from rest_framework import serializers
from vuelos.models import Escala  # Reemplaza 'vuelos' por el nombre real de tu app


class EscalaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Escala
        fields = ['id', 'id_vuelo', 'aeropuerto_escala','image_url']
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