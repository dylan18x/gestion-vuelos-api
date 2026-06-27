from django.contrib import admin
from .models.empleado import Empleado
from .models.piloto import Piloto
from .models.tripulacion import Tripulacion
from .models.asignacion_tripulacion import AsignacionTripulacion
from .models.pista import Pista
from .models.asignacion_pista import AsignacionPista
from .models.torre_control import TorreControl
from .models.autorizacion_vuelo import AutorizacionVuelo

# Registro de cada modelo en el sitio de administración
admin.site.register(Empleado)
admin.site.register(Piloto)
admin.site.register(Tripulacion)
admin.site.register(AsignacionTripulacion)
admin.site.register(Pista)
admin.site.register(AsignacionPista)
admin.site.register(TorreControl)
admin.site.register(AutorizacionVuelo)