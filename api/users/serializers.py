from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name")


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name")

    def validate(self, data):
        try:
            if User.objects.filter(email=data["email"]).exists():
                raise serializers.ValidationError(detail="Invalid value: `email`")
        except User.DoesNotExist:
            pass
        data["is_active"] = True

        return data

    def create(self, validated_data, **kwargs):
        return User.objects.create_user(**validated_data)


class UserAuthenticationSerializer(serializers.Serializer):  # noqa
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ("email", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs["email"], password=attrs["password"])

        if not self.user or not self.user.is_active:
            raise serializers.ValidationError(detail="Authentication failed")

        return attrs
