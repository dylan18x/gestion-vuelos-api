# serializers.py

from rest_framework import serializers
from ..models import PuertaEmbarque

class PuertaEmbarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuertaEmbarque
        fields = '__all__'