from rest_framework import viewsets
from vuelos.models.asignacion_tripulacion import AsignacionTripulacion
from vuelos.serializers.asignacion_tripulacion_serializer import AsignacionTripulacionSerializer
from vuelos.permissions import EsRRHH

class AsignacionTripulacionViewSet(viewsets.ModelViewSet):
    queryset = AsignacionTripulacion.objects.all()
    serializer_class = AsignacionTripulacionSerializer
    permission_classes = [EsRRHH]