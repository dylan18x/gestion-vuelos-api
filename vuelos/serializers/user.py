# vuelos/serializers/user.py
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username  = serializers.CharField(max_length=150)
    email     = serializers.EmailField()
    password  = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('This username is already taken.')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email is already registered.')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            **validated_data
        )
        from vuelos.models.profile import UserProfile

        UserProfile.objects.create(
            user=user
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    num_orders = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    saldo = serializers.SerializerMethodField()  # ← nuevo

    class Meta:
        model  = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_staff', 'is_active', 'date_joined', 'num_orders', 'avatar_url', 'role', 'saldo'
        ]
        read_only_fields = ['id', 'date_joined']

    def get_num_orders(self, obj):
        return 0

    def get_role(self, obj):
        group = obj.groups.first()
        return group.name if group else None

    def get_saldo(self, obj):  # ← nuevo
        try:
            return obj.profile.saldo
        except Exception:
            return 0

    def get_avatar_url(self, obj):
        request = self.context.get('request')
        try:
            avatar = obj.profile.avatar
            if avatar:
                return request.build_absolute_uri(avatar.url) if request else avatar.url
        except Exception:
            pass
        return None


class UserProfileSerializer(serializers.ModelSerializer):
    avatar     = serializers.ImageField(
        source='profile.avatar', required=False, allow_null=True
    )
    avatar_url = serializers.SerializerMethodField()
    saldo      = serializers.SerializerMethodField()  # ← nuevo

    class Meta:
        model  = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'avatar', 'avatar_url', 'saldo']
        read_only_fields = ['id']
        extra_kwargs = {'avatar': {'write_only': True}}

    def get_saldo(self, obj):  # ← nuevo
        try:
            return obj.profile.saldo
        except Exception:
            return 0

    def get_avatar_url(self, obj):
        request = self.context.get('request')
        try:
            avatar = obj.profile.avatar
            if avatar:
                return request.build_absolute_uri(avatar.url) if request else avatar.url
        except Exception:
            pass
        return None



class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password     = serializers.CharField(min_length=8, write_only=True)
    new_password2    = serializers.CharField(write_only=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password is incorrect.')
        return value

    def validate(self, data):
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': 'Passwords do not match.'})
        return data