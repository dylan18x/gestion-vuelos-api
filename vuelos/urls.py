# vuelos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from vuelos.views.health import health_check
from vuelos.views.auth   import RegisterView, LogoutView
from vuelos.views.user   import UserViewSet
from vuelos.serializers.auth import CustomTokenView
from vuelos.views.aereopuerto_views import AeropuertoViewSet
from vuelos.views.terminal_views import TerminalViewSet
from vuelos.views.puerta_embarque_views import PuertaEmbarqueViewSet
from vuelos.views.aereolinea_views import AerolineaViewSet
from vuelos.views.avion_views import AvionViewSet
from vuelos.views.tipo_avion_views import TipoAvionViewSet
from vuelos.views.matenimiento_views import MantenimientoViewSet
from vuelos.views.estado_vuelo_views import EstadoVueloViewSet
from vuelos.views.clima_views import ClimaViewSet


router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register(r'aeropuertos', AeropuertoViewSet)
router.register(r'terminales', TerminalViewSet)
router.register(r'puertas-embarque', PuertaEmbarqueViewSet)
router.register(r'aerolineas', AerolineaViewSet)
router.register(r'aviones', AvionViewSet)
router.register(r'tipos-avion', TipoAvionViewSet)
router.register(r'mantenimientos', MantenimientoViewSet)
router.register(r'Estado_vuelo', EstadoVueloViewSet)
router.register(r'Clima',ClimaViewSet)
urlpatterns = [
    path('health/',             health_check),
    path('auth/register/',      RegisterView.as_view()),
    path('auth/login/',         CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/',  TokenVerifyView.as_view()),
    path('auth/logout/',        LogoutView.as_view()),
    path('', include(router.urls)),
]