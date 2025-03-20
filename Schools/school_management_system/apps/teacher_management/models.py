from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject_specialization = models.CharField(max_length=100)
    hire_date = models.DateField()
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class ClassSchedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_name} - {self.subject} ({self.day_of_week})"

class Leave(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"Leave for {self.teacher.user.first_name} {self.teacher.user.last_name} from {self.start_date} to {self.end_date}"