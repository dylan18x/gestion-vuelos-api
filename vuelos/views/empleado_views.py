from rest_framework import viewsets
from vuelos.models.empleado import Empleado
from vuelos.serializers.empleado_serializer import EmpleadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer