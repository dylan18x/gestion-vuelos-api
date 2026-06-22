from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from vuelos.views.health          import health_check
from vuelos.views.auth            import RegisterView, LogoutView
from vuelos.views.user            import UserViewSet
# — Dylan —
from vuelos.views.vuelo           import VueloViewSet
from vuelos.views.ruta            import RutaViewSet
from vuelos.views.horario         import HorarioViewSet
from vuelos.views.escala          import EscalaViewSet
from vuelos.views.control_trafico import ControlTraficoViewSet
from vuelos.views.registro_vuelo  import RegistroVueloViewSet
from vuelos.views.incidente       import IncidenteViewSet
from vuelos.serializers.auth      import CustomTokenView

router = DefaultRouter()
router.register('users',             UserViewSet,           basename='user')
# — Dylan —
router.register('vuelos',            VueloViewSet,          basename='vuelo')
router.register('rutas',             RutaViewSet,           basename='ruta')
router.register('horarios',          HorarioViewSet,        basename='horario')
router.register('escalas',           EscalaViewSet,         basename='escala')
router.register('controles-trafico', ControlTraficoViewSet, basename='control-trafico')
router.register('registros-vuelo',   RegistroVueloViewSet,  basename='registro-vuelo')
router.register('incidentes',        IncidenteViewSet,      basename='incidente')

urlpatterns = [
    path('health/',             health_check),
    path('auth/register/',      RegisterView.as_view()),
    path('auth/login/',         CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/',  TokenVerifyView.as_view()),
    path('auth/logout/',        LogoutView.as_view()),
    path('', include(router.urls)),
]