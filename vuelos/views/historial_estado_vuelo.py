from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models                             import HistorialEstadoVuelo
from vuelos.serializers.historial_estado_vuelo import HistorialEstadoVueloSerializer
from vuelos.permissions                        import EsOperadorVuelo
from vuelos.filters                            import HistorialEstadoVueloFilter
from vuelos.pagination                         import StandardPagination


class HistorialEstadoVueloViewSet(viewsets.ModelViewSet):
    queryset           = HistorialEstadoVuelo.objects.select_related('id_vuelo', 'id_estado').all()
    serializer_class   = HistorialEstadoVueloSerializer
    permission_classes = [EsOperadorVuelo]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_class    = HistorialEstadoVueloFilter
    ordering_fields    = ['fecha_cambio']
    ordering           = ['-fecha_cambio']