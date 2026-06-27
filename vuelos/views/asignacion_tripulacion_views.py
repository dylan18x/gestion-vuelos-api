from rest_framework import viewsets
from vuelos.models.asignacion_tripulacion import AsignacionTripulacion
from vuelos.serializers.asignacion_tripulacion_serializer import AsignacionTripulacionSerializer

class AsignacionTripulacionViewSet(viewsets.ModelViewSet):
    queryset = AsignacionTripulacion.objects.all()
    serializer_class = AsignacionTripulacionSerializer