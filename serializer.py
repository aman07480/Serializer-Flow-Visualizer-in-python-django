from rest_framework import serializers
from .mixins import SerializerFlowMixin


class ProductSerializer(SerializerFlowMixin, serializers.Serializer):

    name = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):

        return validated_data

class SerializerFlowLog(models.Model):
    step = models.CharField(max_length=200)
    data = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)