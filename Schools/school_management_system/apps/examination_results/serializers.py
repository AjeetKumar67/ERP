from rest_framework import serializers
from .models import Exam, Marks, ReportCard

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name', 'date', 'class_assigned', 'created_at']

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ['id', 'exam', 'student', 'marks_obtained']

class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = ['id', 'student', 'exam', 'total_marks', 'grade', 'remarks']