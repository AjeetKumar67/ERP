from rest_framework import serializers
from .models import ClassSession, Assignment, OnlineClassMaterial, Attendance

class ClassSessionSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = ClassSession
        fields = ['id', 'title', 'description', 'start_time', 'end_time', 'teacher', 'students']

class AssignmentSerializer(serializers.ModelSerializer):
    class_session = serializers.StringRelatedField()
    submitted_by = serializers.StringRelatedField()

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_date', 'class_session', 'submitted_by']

class OnlineClassMaterialSerializer(serializers.ModelSerializer):
    class_session = serializers.StringRelatedField()

    class Meta:
        model = OnlineClassMaterial
        fields = ['id', 'class_session', 'file', 'uploaded_at']

class AttendanceSerializer(serializers.ModelSerializer):
    class_session = serializers.StringRelatedField()
    student = serializers.StringRelatedField()

    class Meta:
        model = Attendance
        fields = ['id', 'class_session', 'student', 'date', 'status']