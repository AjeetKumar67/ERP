from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='classes')

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
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name