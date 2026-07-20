import uuid

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from vuelos.models import Reserva
from vuelos.serializers.reserva_serializer import ReservaSerializer


class ReservaViewSet(viewsets.ModelViewSet):

    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reserva.objects.filter(
            usuario=self.request.user
        )

    def perform_create(self, serializer):

        vuelo = serializer.validated_data['vuelo']

        pasajeros = serializer.validated_data.get(
            'cantidad_pasajeros',
            1
        )

        if vuelo.asientos_disponibles < pasajeros:
            raise serializer.ValidationError(
                'No hay suficientes asientos.'
            )

        vuelo.asientos_disponibles -= pasajeros

        vuelo.save()

        serializer.save(
            usuario=self.request.user,
            codigo_reserva=str(uuid.uuid4())[:8].upper(),
            precio_total=vuelo.precio * pasajeros
        )