from django.db import models
from django.utils import timezone
from apps.student_management.models import Student
from apps.teacher_management.models import Teacher

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')])
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

class Biometric(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('In', 'In'), ('Out', 'Out')])

    def __str__(self):
        return f"{self.student} - {self.timestamp} - {self.status}"