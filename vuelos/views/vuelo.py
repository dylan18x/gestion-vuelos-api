from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vuelos.models               import Vuelo
from vuelos.serializers.vuelo    import VueloSerializer
from vuelos.permissions          import IsStaffOrReadOnly
from vuelos.filters              import VueloFilter
from vuelos.pagination           import StandardPagination


class VueloViewSet(viewsets.ModelViewSet):
    queryset           = Vuelo.objects.select_related('id_avion').all()
    serializer_class   = VueloSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class    = VueloFilter
    search_fields      = ['codigo_vuelo', 'estado']
    ordering_fields    = ['fecha', 'codigo_vuelo', 'estado']
    ordering           = ['fecha']

    @action(detail=True, methods=['get'], url_path='horarios')
    def horarios(self, request, pk=None):
        vuelo = self.get_object()
        from vuelos.serializers.horario import HorarioSerializer
        serializer = HorarioSerializer(vuelo.horarios.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='incidentes')
    def incidentes(self, request, pk=None):
        vuelo = self.get_object()
        from vuelos.serializers.incidente import IncidenteSerializer
        serializer = IncidenteSerializer(vuelo.incidentes.all(), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        qs = Vuelo.objects.all()
        resumen = {}
        for estado, label in Vuelo.ESTADO_CHOICES:
            resumen[estado] = qs.filter(estado=estado).count()
        return Response({
            'total':      qs.count(),
            'por_estado': resumen,
        })