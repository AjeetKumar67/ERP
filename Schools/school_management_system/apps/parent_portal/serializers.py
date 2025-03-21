from rest_framework import serializers
from .models import ChildProgress, PaymentAlert
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ChildProgressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ChildProgress
        fields = ['id', 'user', 'child_name', 'grade', 'progress_report', 'created_at']

class PaymentAlertSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PaymentAlert
        fields = ['id', 'user', 'amount_due', 'due_date', 'is_paid', 'created_at']