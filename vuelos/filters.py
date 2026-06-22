import django_filters
from vuelos.models import (
    Vuelo, Ruta, Horario, Escala,
    ControlTrafico, RegistroVuelo, Incidente,
)


class VueloFilter(django_filters.FilterSet):
    codigo_vuelo = django_filters.CharFilter(lookup_expr='icontains')
    fecha_desde  = django_filters.DateFilter(field_name='fecha', lookup_expr='gte')
    fecha_hasta  = django_filters.DateFilter(field_name='fecha', lookup_expr='lte')

    class Meta:
        model  = Vuelo
        fields = ['estado', 'id_avion']


class RutaFilter(django_filters.FilterSet):
    class Meta:
        model  = Ruta
        fields = ['origen', 'destino']


class HorarioFilter(django_filters.FilterSet):
    class Meta:
        model  = Horario
        fields = ['id_vuelo']


class EscalaFilter(django_filters.FilterSet):
    class Meta:
        model  = Escala
        fields = ['id_vuelo', 'aeropuerto_escala']


class ControlTraficoFilter(django_filters.FilterSet):
    class Meta:
        model  = ControlTrafico
        fields = ['id_vuelo']


class RegistroVueloFilter(django_filters.FilterSet):
    class Meta:
        model  = RegistroVuelo
        fields = ['id_vuelo']


class IncidenteFilter(django_filters.FilterSet):
    fecha_desde = django_filters.DateFilter(field_name='fecha', lookup_expr='gte')
    fecha_hasta = django_filters.DateFilter(field_name='fecha', lookup_expr='lte')

    class Meta:
        model  = Incidente
        fields = ['id_vuelo']