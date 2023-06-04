from djoser import utils
from djoser.conf import settings as djoser_settings
from djoser.views import TokenCreateView
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.users.serializers import (
    RegistrationSerializer,
    UserAuthenticationSerializer,
    UserSerializer,
)
from apps.users.models import User
from core.permissions import IsOwnerOrIsAdmin


class UserView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
    TokenCreateView,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = {
        "list": (permissions.IsAuthenticated,),
        "retrieve": (IsOwnerOrIsAdmin,),
        "register": (permissions.AllowAny,),
        "login": (permissions.AllowAny,),
        "update": (IsOwnerOrIsAdmin,),
        "destroy": (IsOwnerOrIsAdmin,),
        None: (permissions.AllowAny,),
    }
    serializer_for_action = {
        "update": UserSerializer,
        "register": RegistrationSerializer,
        None: UserAuthenticationSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_for_action.get(self.action) or self.serializer_class

    def get_permissions(self):
        return [permission() for permission in self.permission_classes[self.action]]

    @action(methods=("POST",), detail=False, url_name="register")
    def register(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = utils.login_user(self.request, user)
        token_serializer_class = djoser_settings.SERIALIZERS.token

        data = {
            **self.serializer_class(user).data,
            "token": token_serializer_class(token).data["auth_token"],
        }

        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=("POST",), detail=False, url_name="login")
    def _action(self, serializer):
        user = serializer.user

        token = utils.login_user(self.request, user)
        token_serializer_class = djoser_settings.SERIALIZERS.token

        data = {
            **self.serializer_class(user).data,
            "token": token_serializer_class(token).data["auth_token"],
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "ok"}, status=status.HTTP_200_OK)
