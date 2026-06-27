import django_filters
from .models.empleado import Empleado
from .models.piloto import Piloto
from .models.tripulacion import Tripulacion
from .models.pista import Pista
from .models.torre_control import TorreControl

class EmpleadoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Empleado
        fields = ['nombre', 'cargo']

class PilotoFilter(django_filters.FilterSet):
    licencia = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Piloto
        fields = ['licencia']

class TripulacionFilter(django_filters.FilterSet):
    class Meta:
        model = Tripulacion
        fields = ['cargo']

class PistaFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Pista
        fields = ['codigo', 'estado']

class TorreControlFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = TorreControl
        fields = ['nombre', 'id_aeropuerto']