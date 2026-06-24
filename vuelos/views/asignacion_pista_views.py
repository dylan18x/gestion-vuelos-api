from rest_framework import viewsets
from vuelos.models.asignacion_pista import AsignacionPista
from vuelos.serializers.asignacion_pista_serializer import AsignacionPistaSerializer

class AsignacionPistaViewSet(viewsets.ModelViewSet):
    queryset = AsignacionPista.objects.all()
    serializer_class = AsignacionPistaSerializer