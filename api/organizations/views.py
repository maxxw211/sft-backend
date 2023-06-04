from rest_framework import mixins, permissions, viewsets

from api.organizations.serializers import OrganizationSerializer
from apps.organizations.models import Organization
from core.permissions import IsOwner


class OrganizationView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = {
        "list": (permissions.IsAuthenticated,),
        "retrieve": (permissions.IsAuthenticated,),
        "create": (permissions.IsAuthenticated,),
        "update": (IsOwner,),
        "partial_update": (IsOwner,),
        "destroy": (IsOwner,),
        "organization_data": (IsOwner,),
        None: (permissions.AllowAny,),
    }
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def get_permissions(self):
        return [permission() for permission in self.permission_classes[self.action]]
