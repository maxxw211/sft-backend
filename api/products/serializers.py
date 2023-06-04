from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "label",
            "vendor_code",
            "manufacturer",
            "credit_application_id",
            "created_at",
        )

    def validate(self, attrs):
        owner = self.context.get("request").user
        manufacturer = attrs.get("manufacturer")

        if manufacturer.owner != owner:
            raise serializers.ValidationError(
                detail="The vendor ID you entered does not match the organization you own."
            )
        return attrs
