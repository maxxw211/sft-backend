from rest_framework import permissions, mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.credit_applications.serializers import (
    CreditApplicationSerializer,
    CreditApplicationContractSerializer,
)

from apps.credit_applications.models import CreditApplication
from core.permissions import IsOwner


class CreditApplicationView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = {
        "list": (permissions.IsAuthenticated,),
        "retrieve": (permissions.IsAuthenticated,),
        "create": (permissions.IsAuthenticated,),
        "destroy": (IsOwner,),
        "organization_data": (IsOwner,),
        None: (permissions.AllowAny,),
    }
    serializer_class = CreditApplicationSerializer
    queryset = CreditApplication.objects.all()

    @action(methods=("POST",), detail=True, url_name="organization_data")
    def organization_data(self, request, *args, **kwargs):
        serializer = CreditApplicationContractSerializer(
            data=request.data, context={"credit_application_id": kwargs["pk"]}
        )
        serializer.is_valid(raise_exception=True)
        contract_id = serializer.validated_data

        """
         I left this commented out code here as an example that it is possible to get the queryset in a different way.
        """
        # queryset = self.queryset.filter(contract_id=contract_id).prefetch_related(
        #     Prefetch("products", queryset=Product.objects.select_related("manufacturer"))
        # ).values_list("products__manufacturer", flat=True).distinct()

        queryset = (
            self.queryset.filter(contract_id=contract_id)
            .prefetch_related("products__manufacturer")
            .values_list("products__manufacturer", flat=True)
        )

        return Response(
            data={"manufacturer_ids is": queryset}, status=status.HTTP_200_OK
        )

    def get_permissions(self):
        return [permission() for permission in self.permission_classes[self.action]]
