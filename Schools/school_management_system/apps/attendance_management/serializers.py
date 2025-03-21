from rest_framework import serializers
from .models import Attendance, Biometric

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'date', 'status', 'remarks']

class BiometricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biometric
        fields = ['id', 'student', 'timestamp', 'status']