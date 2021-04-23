from rest_framework import serializers

from controller.models import RobotStatus, Position, Package


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotStatus
        fields = ("id", "status", "time")

        extra_kwargs = {
            'status': {'read_only': True},
            'time': {'read_only': True},
        }


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ("id", "name", "position_number", "status", "time_info_updated")


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ("id", "name", "status", "position", "time_arrived", "time_of_departure", "additional_info")
