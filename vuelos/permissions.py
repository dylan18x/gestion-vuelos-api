# vuelos/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  
        return bool(request.user and request.user.is_staff)

class EsControlador(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_staff:
            return True
        return request.user.groups.filter(
            name="CONTROLADOR"
        ).exists()


class EsTecnico(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_staff:
            return True
        return request.user.groups.filter(
            name="TECNICO"
        ).exists()


class EsRRHH(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_staff:
            return True
        return request.user.groups.filter(
            name="RRHH"
        ).exists()


class EsOperadorVuelo(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_staff:
            return True
        return request.user.groups.filter(
            name="OPERADOR_VUELO"
        ).exists()