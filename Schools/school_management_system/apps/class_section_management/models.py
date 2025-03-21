from django.db import models

class ClassSection(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='class_sections')

    def __str__(self):
        return f"{self.name} - {self.grade}"

class Section(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    subjects = models.ManyToManyField(Subject, related_name='teachers')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

class Timetable(models.Model):
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE, related_name='timetables')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetables')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='timetables')
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_section} - {self.subject} - {self.day_of_week}"

class Class(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)