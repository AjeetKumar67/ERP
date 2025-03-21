from django.db import models
from apps.student_management.models import Student
from apps.teacher_management.models import Teacher
from apps.class_section_management.models import ClassSection

class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    class_assigned = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Marks(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.marks_obtained}"

class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    total_marks = models.FloatField()
    grade = models.CharField(max_length=2)
    remarks = models.TextField()

    def __str__(self):
        return f"Report Card for {self.student} - {self.exam}"