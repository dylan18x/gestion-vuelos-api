from django.contrib import admin
from vuelos.models import (
    Vuelo, Ruta, Horario, Escala,
    ControlTrafico, RegistroVuelo, Incidente,
)


@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display  = ['id', 'codigo_vuelo', 'fecha', 'estado', 'id_avion']
    list_filter   = ['estado', 'fecha']
    search_fields = ['codigo_vuelo']


@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ['id', 'origen', 'destino']
    list_filter  = ['origen', 'destino']


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_vuelo', 'salida_programada', 'llegada_programada']
    list_filter  = ['salida_programada']


@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_vuelo', 'aeropuerto_escala']


@admin.register(ControlTrafico)
class ControlTraficoAdmin(admin.ModelAdmin):
    list_display  = ['id', 'id_vuelo', 'autorizacion', 'hora']
    list_filter   = ['hora']
    search_fields = ['autorizacion']


@admin.register(RegistroVuelo)
class RegistroVueloAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_vuelo', 'hora_real_salida', 'hora_real_llegada']


@admin.register(Incidente)
class IncidenteAdmin(admin.ModelAdmin):
    list_display  = ['id', 'id_vuelo', 'fecha', 'descripcion']
    list_filter   = ['fecha']
    search_fields = ['descripcion']

from vuelos.models import HistorialEstadoVuelo

@admin.register(HistorialEstadoVuelo)
class HistorialEstadoVueloAdmin(admin.ModelAdmin):
    list_display  = ['id', 'id_vuelo', 'id_estado', 'fecha_cambio']
    list_filter   = ['id_estado', 'fecha_cambio']
    search_fields = ['observacion']
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
