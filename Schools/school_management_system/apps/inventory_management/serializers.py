from rest_framework import serializers
from .models import Supply, Uniform

class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ['id', 'name', 'quantity', 'unit_price', 'total_price', 'date_added']
        read_only_fields = ['total_price', 'date_added']

class UniformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uniform
        fields = ['id', 'type', 'size', 'quantity', 'price', 'date_added']
        read_only_fields = ['date_added']