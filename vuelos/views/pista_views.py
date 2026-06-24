from rest_framework import viewsets
from vuelos.models.pista import Pista
from vuelos.serializers.pista_serializer import PistaSerializer

class PistaViewSet(viewsets.ModelViewSet):
    queryset = Pista.objects.all()
    serializer_class = PistaSerializer