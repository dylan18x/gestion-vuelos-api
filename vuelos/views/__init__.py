from .aereolinea_views import *
from .aereopuerto_views import * # Con dos 'e'
from .auth import *
from .avion_views import *
from .health import *
from .matenimiento_views import * # Sin la primera 'n', tal como tu archivo
from .puerta_embarque_views import *
from .terminal_views import *
from .estado_vuelo_views import *
from .clima_views import *
# Si tienes tipo_avion_views.py más abajo en esa carpeta, agrégalo aquí:
# from .tipo_avion_views import * ```

from rest_framework import viewsets
from ..models import Aeropuerto
from ..serializers import * # Usar el asterisco ayuda a evitar fallos por nombres individuales mientras se prueba