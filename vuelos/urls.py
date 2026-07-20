from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

# Auth y utilidades
from vuelos.views.health import health_check
from vuelos.views.auth import RegisterView, LogoutView
from vuelos.views.user import UserViewSet
from vuelos.serializers.auth import CustomTokenView
from django.conf import settings
from django.conf.urls.static import static


# Historial
from vuelos.views.historial_estado_vuelo import HistorialEstadoVueloViewSet

# — Alejandro —
from vuelos.views.aeropuerto_views import AeropuertoViewSet
from vuelos.views.terminal_views import TerminalViewSet
from vuelos.views.puerta_embarque_views import PuertaEmbarqueViewSet
from vuelos.views.aerolinea_views import AerolineaViewSet
from vuelos.views.avion_views import AvionViewSet
from vuelos.views.tipo_avion_views import TipoAvionViewSet
from vuelos.views.matenimiento_views import MantenimientoViewSet
from vuelos.views.estado_vuelo_views import EstadoVueloViewSet
from vuelos.views.clima_views import ClimaViewSet

# — Dylan —
from vuelos.views.vuelo import VueloViewSet
from vuelos.views.ruta import RutaViewSet
from vuelos.views.horario import HorarioViewSet
from vuelos.views.escala import EscalaViewSet
from vuelos.views.control_trafico import ControlTraficoViewSet
from vuelos.views.registro_vuelo import RegistroVueloViewSet
from vuelos.views.incidente import IncidenteViewSet
from vuelos.views.reserva_view import ReservaViewSet

from vuelos.views import (
    EmpleadoViewSet,
    PilotoViewSet,
    TripulacionViewSet,
    AsignacionTripulacionViewSet,
    PistaViewSet,
    AsignacionPistaViewSet,
    TorreControlViewSet,
    AutorizacionVueloViewSet
)

router = DefaultRouter()

# Usuarios
router.register('users', UserViewSet, basename='user')

# — Alejandro —
router.register('aeropuertos', AeropuertoViewSet, basename='aeropuerto')
router.register('terminales', TerminalViewSet, basename='terminal')
router.register('puertas-embarque', PuertaEmbarqueViewSet, basename='puerta-embarque')
router.register('aerolineas', AerolineaViewSet, basename='aerolinea')
router.register('aviones', AvionViewSet, basename='avion')
router.register('tipos-avion', TipoAvionViewSet, basename='tipo-avion')
router.register('mantenimientos', MantenimientoViewSet, basename='mantenimiento')
router.register('Estado_vuelo', EstadoVueloViewSet, basename='estado-vuelo')
router.register('Clima', ClimaViewSet, basename='clima')

# — Dylan —
router.register('vuelos', VueloViewSet, basename='vuelos')
router.register('rutas', RutaViewSet, basename='ruta')
router.register('horarios', HorarioViewSet, basename='horario')
router.register('escalas', EscalaViewSet, basename='escala')
router.register('controles-trafico', ControlTraficoViewSet, basename='control-trafico')
router.register('registros-vuelo', RegistroVueloViewSet, basename='registro-vuelo')
router.register('incidentes', IncidenteViewSet, basename='incidente')

# Otros
router.register('empleados', EmpleadoViewSet, basename='empleado')
router.register('pilotos', PilotoViewSet, basename='piloto')
router.register('tripulacion', TripulacionViewSet, basename='tripulacion')
router.register(
    'asignacion-tripulacion',
    AsignacionTripulacionViewSet,
    basename='asignacion-tripulacion'
)
router.register('pistas', PistaViewSet, basename='pista')
router.register(
    'asignacion-pista',
    AsignacionPistaViewSet,
    basename='asignacion-pista'
)
router.register('torres-control', TorreControlViewSet, basename='torre-control')
router.register(
    'autorizaciones-vuelo',
    AutorizacionVueloViewSet,
    basename='autorizacion-vuelo'
)
router.register(
    'historial-estados-vuelo',
    HistorialEstadoVueloViewSet,
    basename='historial-estado-vuelo'
)
router.register(
    'reservas',
    ReservaViewSet,
    basename='reservas'
)


urlpatterns = [
    path('health/', health_check),

    # Auth
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/', TokenVerifyView.as_view()),
    path('auth/logout/', LogoutView.as_view()),

    # API
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)