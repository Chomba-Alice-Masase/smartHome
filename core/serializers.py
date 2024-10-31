# In this case we are serializing the data from our sensors.

from rest_framework import serializers
from core.models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

