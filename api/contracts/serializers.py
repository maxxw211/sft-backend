from rest_framework import serializers

from apps.contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ("id", "text", "number", "created_at")
