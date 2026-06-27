from rest_framework import viewsets
from vuelos.models.tripulacion import Tripulacion
from vuelos.serializers.tripulacion_serializer import TripulacionSerializer

class TripulacionViewSet(viewsets.ModelViewSet):
    queryset = Tripulacion.objects.all()
    serializer_class = TripulacionSerializer