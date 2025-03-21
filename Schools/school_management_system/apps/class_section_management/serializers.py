from rest_framework import serializers
from .models import ClassSection, Section, Subject, Teacher, Student, Timetable

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name', 'capacity']

class ClassSectionSerializer(serializers.ModelSerializer):
    section_name = serializers.ReadOnlyField(source='section.name')

    class Meta:
        model = ClassSection
        fields = ['id', 'name', 'grade', 'section', 'section_name']

class SubjectSerializer(serializers.ModelSerializer):
    class_section_name = serializers.ReadOnlyField(source='class_section.name')

    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'class_section', 'class_section_name']

class TeacherSerializer(serializers.ModelSerializer):
    subject_names = serializers.StringRelatedField(many=True, source='subjects')

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'employee_id', 'subjects', 'subject_names']

class StudentSerializer(serializers.ModelSerializer):
    class_section_name = serializers.ReadOnlyField(source='class_section.name')

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_number', 'class_section', 'class_section_name']

class TimetableSerializer(serializers.ModelSerializer):
    class_section_name = serializers.ReadOnlyField(source='class_section.name')
    subject_name = serializers.ReadOnlyField(source='subject.name')
    teacher_name = serializers.ReadOnlyField(source='teacher.name')

    class Meta:
        model = Timetable
        fields = [
            'id', 'class_section', 'class_section_name', 'subject', 'subject_name',
            'teacher', 'teacher_name', 'day_of_week', 'start_time', 'end_time'
        ]