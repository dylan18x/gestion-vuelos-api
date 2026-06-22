# views.py

from rest_framework import viewsets
from ..models import Aeropuerto
from ..serializers import AeropuertoSerializer

class AeropuertoViewSet(viewsets.ModelViewSet):
    queryset = Aeropuerto.objects.all()
    serializer_class = AeropuertoSerializer