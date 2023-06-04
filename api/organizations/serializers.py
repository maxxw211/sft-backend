from rest_framework import serializers

from apps.organizations.models import Organization
from apps.users.models import User


class OrganizationSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
    )

    class Meta:
        model = Organization
        fields = ("id", "name", "code", "email", "created_at", "owner")

    def validate(self, attrs):
        owner = attrs.get("user") or self.context.get("request").user
        if owner != self.context.get("request").user:
            raise serializers.ValidationError(
                detail="The entered email does not match the registered user"
            )
        attrs["owner"] = owner
        return attrs
