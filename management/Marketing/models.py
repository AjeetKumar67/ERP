from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('planned', 'Planned'), ('running', 'Running'), ('completed', 'Completed')])
