from rest_framework import serializers

from controller.models import RobotStatus


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotStatus
        fields = ("status", "time")

        extra_kwargs = {
            'status': {'read_only': True},
            'time': {'read_only': True},
        }
