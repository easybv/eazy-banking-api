from rest_framework import serializers
from .models import DeliveryDetails


class DeliverySerializer(serializers.ModelSerializer):
    total_volumetric_weight = serializers.SerializerMethodField(
        method_name='get_volumetric_weight',
    )
    total_volume = serializers.SerializerMethodField(
        method_name='get_total_volume',
    )
    total_actual_weight = serializers.SerializerMethodField(
        method_name='get_total_actual_weight',
    )

    class Meta:
        model = DeliveryDetails
        fields = "__all__"

    def get_volumetric_weight(self, instance):
        total_volumetric = instance.height * instance.width * instance.weight
        return total_volumetric

    def get_total_volume(self, instance):
        total_volume = instance.height * instance.width * instance.length
        return total_volume

    def get_total_actual_weight(self, instance):
        total_actual_weight = instance.height * \
            instance.width * instance.length * instance.weight
        return total_actual_weight
