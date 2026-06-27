# serializers.py

from rest_framework import serializers
from ..models import TipoAvion

class TipoAvionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAvion
        fields = '__all__'