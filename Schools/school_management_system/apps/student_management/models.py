from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()
    admission_date = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    class_enrolled = models.ForeignKey('class_section_management.Class', on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey('class_section_management.Section', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.roll_number}"

class Admission(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    admission_fee = models.DecimalField(max_digits=10, decimal_places=2)
    documents_submitted = models.BooleanField(default=False)
    admission_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"Admission for {self.student.user.first_name} {self.student.user.last_name}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"Attendance for {self.student.user.first_name} on {self.date}"