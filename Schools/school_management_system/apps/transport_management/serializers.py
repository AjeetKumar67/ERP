from rest_framework import serializers
from .models import BusRoute, Driver, DriverAssignment, TransportRequest

class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute
        fields = ['id', 'route_name', 'starting_point', 'destination', 'stops', 'distance']


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'license_number', 'phone_number', 'email']


class DriverAssignmentSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)
    bus_route = BusRouteSerializer(read_only=True)

    class Meta:
        model = DriverAssignment
        fields = ['id', 'driver', 'bus_route', 'assigned_date', 'end_date']


class TransportRequestSerializer(serializers.ModelSerializer):
    bus_route = BusRouteSerializer(read_only=True)

    class Meta:
        model = TransportRequest
        fields = ['id', 'student_name', 'bus_route', 'request_date', 'status']