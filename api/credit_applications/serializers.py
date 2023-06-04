from rest_framework import serializers

from django.forms.models import model_to_dict

from apps.contracts.models import Contract
from apps.credit_applications.models import CreditApplication
from apps.products.models import Product


class CreditApplicationContractSerializer(serializers.Serializer):
    contract = serializers.IntegerField(required=True)

    def validate(self, attrs):
        credit_application_id = self.context["credit_application_id"]
        contract_id = attrs["contract"]

        if not Contract.objects.filter(
            id=contract_id, credit_application=credit_application_id
        ).exists():
            raise serializers.ValidationError(detail="Invalid contract id")

        return contract_id


class CreditApplicationSerializer(serializers.ModelSerializer):
    products = serializers.ListSerializer(
        child=serializers.IntegerField(), required=True
    )

    class Meta:
        model = CreditApplication
        fields = ("id", "number", "contract", "products", "created_at")

    def create(self, validated_data):
        user = self.context["request"].user
        product_ids = validated_data.pop("products")
        products = Product.objects.filter(id__in=product_ids).exclude(
            credit_application_id__isnull=True
        )
        if products.exists():
            raise serializers.ValidationError(detail="Invalid product ids")

        instance = CreditApplication.objects.create(**validated_data)
        instance.products.add(*products)

        user.is_owner = True
        user.save()

        return instance

    def to_representation(self, instance):
        return model_to_dict(instance)
