from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email']    = user.email
        token['is_staff'] = user.is_staff
        group = user.groups.first()
        token['role'] = group.name if group else None
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        group = self.user.groups.first()

        data['user_id']   = self.user.id
        data['id']        = self.user.id          # 👈 para que Flutter lo reconozca
        data['username']  = self.user.username
        data['email']     = self.user.email
        data['first_name']= self.user.first_name   # 👈 opcional, para el saludo
        data['last_name'] = self.user.last_name    # 👈 opcional
        data['is_staff']  = self.user.is_staff
        data['role']      = group.name if group else None  # 👈 el que faltaba
        return data


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer