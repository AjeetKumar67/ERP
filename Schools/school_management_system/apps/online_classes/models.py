from django.db import models
from django.contrib.auth.models import User

class ClassSession(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    teacher = models.ForeignKey('teacher_management.Teacher', on_delete=models.CASCADE)
    students = models.ManyToManyField('student_management.Student', related_name='class_sessions')

    def __str__(self):
        return self.title

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    class_session = models.ForeignKey(ClassSession, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class OnlineClassMaterial(models.Model):
    class_session = models.ForeignKey(ClassSession, on_delete=models.CASCADE)
    file = models.FileField(upload_to='class_materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Material for {self.class_session.title}'

class Attendance(models.Model):
    class_session = models.ForeignKey(ClassSession, on_delete=models.CASCADE)
    student = models.ForeignKey(
        'student_management.Student',
        on_delete=models.CASCADE,
        related_name='online_class_attendance'  # Add related_name
    )
    date = models.DateField()
    status = models.BooleanField(default=False)  # True for present, False for absent

    def __str__(self):
        return f'Attendance for {self.student} in {self.class_session.title}'