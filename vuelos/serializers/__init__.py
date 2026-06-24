# vuelos/serializers/__init__.py
from .auth import CustomTokenSerializer, CustomTokenView
from .user import (
    RegisterSerializer,
    UserSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
)

from .empleado_serializer import EmpleadoSerializer
from .piloto_serializer import PilotoSerializer
from .tripulacion_serializer import TripulacionSerializer
from .asignacion_tripulacion_serializer import AsignacionTripulacionSerializer
from .pista_serializer import PistaSerializer
from .asignacion_pista_serializer import AsignacionPistaSerializer