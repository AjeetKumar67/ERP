from rest_framework import serializers
from .models import Teacher, ClassSchedule, Leave
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'subject_specialization', 'hire_date', 'phone_number', 'address']

class ClassScheduleSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = ClassSchedule
        fields = ['id', 'teacher', 'class_name', 'subject', 'day_of_week', 'start_time', 'end_time']

class LeaveSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Leave
        fields = ['id', 'teacher', 'start_date', 'end_date', 'reason', 'status']