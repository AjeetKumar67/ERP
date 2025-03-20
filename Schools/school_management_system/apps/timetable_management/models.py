from django.db import models
from apps.class_section_management.models import Class, Section
from apps.teacher_management.models import Teacher

class Timetable(models.Model):
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('class_instance', 'section', 'day_of_week', 'start_time')

    def __str__(self):
        return f"{self.class_instance} - {self.subject} ({self.day_of_week})"

class Schedule(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    week_number = models.IntegerField()
    term = models.CharField(max_length=20)

    def __str__(self):
        return f"Schedule for {self.timetable} - Week {self.week_number} ({self.term})"