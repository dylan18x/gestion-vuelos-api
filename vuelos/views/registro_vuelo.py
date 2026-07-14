from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models                     import RegistroVuelo
from vuelos.serializers.registro_vuelo import RegistroVueloSerializer
from vuelos.permissions                import EsOperadorVuelo
from vuelos.filters                    import RegistroVueloFilter
from vuelos.pagination                 import StandardPagination


class RegistroVueloViewSet(viewsets.ModelViewSet):
    queryset           = RegistroVuelo.objects.select_related('id_vuelo').all()
    serializer_class   = RegistroVueloSerializer
    permission_classes = [EsOperadorVuelo]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_class    = RegistroVueloFilter
    ordering_fields    = ['hora_real_salida', 'hora_real_llegada']
    ordering           = ['hora_real_salida']