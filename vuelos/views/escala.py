from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models             import Escala
from vuelos.serializers.escala import EscalaSerializer
from vuelos.permissions        import EsOperadorVuelo
from vuelos.filters            import EscalaFilter
from vuelos.pagination         import StandardPagination


class EscalaViewSet(viewsets.ModelViewSet):
    queryset           = Escala.objects.select_related('id_vuelo', 'aeropuerto_escala').all()
    serializer_class   = EscalaSerializer
    permission_classes = [EsOperadorVuelo]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_class    = EscalaFilter
    ordering_fields    = ['id_vuelo']
    ordering           = ['id_vuelo']