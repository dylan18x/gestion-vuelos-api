from .auth import CustomTokenSerializer, CustomTokenView
from .user import (
    RegisterSerializer,
    UserSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
)

# Serializadores de tu app (copiados exactamente de tus nombres de archivo)
from .aereolinea_serializer import *
from .aereopuerto_serializer import * # Con dos 'e' como tu archivo físico
from .avion_serializer import *
from .mantenimiento_serializer import *
from .puerta_embarque_serializer import *
from .terminal_serializer import *
from .tipo_avion_serializer import *