from rest_framework import mixins, permissions, viewsets

from api.contracts.serializers import ContractSerializer
from apps.contracts.models import Contract


class ContractView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
