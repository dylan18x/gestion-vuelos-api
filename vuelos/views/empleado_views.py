from rest_framework import viewsets
from vuelos.models.empleado import Empleado
from vuelos.serializers.empleado_serializer import EmpleadoSerializer
from vuelos.permissions import EsRRHH

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [EsRRHH]