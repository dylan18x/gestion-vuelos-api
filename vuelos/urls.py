# vuelos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from vuelos.views.health import health_check
from vuelos.views.auth   import RegisterView, LogoutView
from vuelos.views.user   import UserViewSet
from vuelos.serializers.auth import CustomTokenView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('health/',             health_check),
    path('auth/register/',      RegisterView.as_view()),
    path('auth/login/',         CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/',  TokenVerifyView.as_view()),
    path('auth/logout/',        LogoutView.as_view()),
    path('', include(router.urls)),
]