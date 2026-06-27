from .auth import CustomTokenSerializer, CustomTokenView
from .user import (
    RegisterSerializer,
    UserSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
)
# — Dylan —
from .vuelo           import VueloSerializer
from .ruta            import RutaSerializer
from .horario         import HorarioSerializer
from .escala          import EscalaSerializer
from .control_trafico import ControlTraficoSerializer
from .registro_vuelo  import RegistroVueloSerializer
from .incidente       import IncidenteSerializer

# Serializadores de tu app (copiados exactamente de tus nombres de archivo)
from .aereolinea_serializer import *
from .aereopuerto_serializer import * # Con dos 'e' como tu archivo físico
from .avion_serializer import *
from .mantenimiento_serializer import *
from .puerta_embarque_serializer import *
from .terminal_serializer import *
from .tipo_avion_serializer import *
from .clima_serializer import *
from .estado_vuelo_serializer import *

from .empleado_serializer import EmpleadoSerializer
from .piloto_serializer import PilotoSerializer
from .tripulacion_serializer import TripulacionSerializer
from .asignacion_tripulacion_serializer import AsignacionTripulacionSerializer
from .pista_serializer import PistaSerializer
from .asignacion_pista_serializer import AsignacionPistaSerializer  
from .torre_control_serializer import TorreControlSerializer  
from .autorizacion_vuelo_serializer import AutorizacionVueloSerializer 
from .historial_estado_vuelo import HistorialEstadoVueloSerializer
