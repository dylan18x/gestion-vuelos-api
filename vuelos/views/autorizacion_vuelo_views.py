from rest_framework import viewsets
from vuelos.models.autorizacion_vuelo import AutorizacionVuelo
from vuelos.serializers.autorizacion_vuelo_serializer import AutorizacionVueloSerializer
from vuelos.permissions import IsStaffOrReadOnly

class AutorizacionVueloViewSet(viewsets.ModelViewSet):
    queryset = AutorizacionVuelo.objects.all()
    serializer_class = AutorizacionVueloSerializer
    permission_classes = [IsStaffOrReadOnly]