from rest_framework import mixins, permissions, viewsets

from api.products.serializers import ProductSerializer
from apps.products.models import Product
from core.permissions import IsOwner


class ProductView(
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
        "create": (IsOwner,),
        "update": (IsOwner,),
        "partial_update": (IsOwner,),
        "destroy": (IsOwner,),
        "organization_data": (IsOwner,),
        None: (permissions.AllowAny,),
    }
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        return [permission() for permission in self.permission_classes[self.action]]
