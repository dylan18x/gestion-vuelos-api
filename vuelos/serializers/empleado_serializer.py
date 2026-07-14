from rest_framework import serializers
from vuelos.models.empleado import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Empleado
        fields = ['id_empleado', 'nombre', 'cargo','image_url']
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
        representation['id'] = representation.pop('id_empleado')
        return representation