from django.db import models
from management.SalesCRM.models import Customer

# Create your models here.
class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    issue = models.TextField()
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')])
    created_at = models.DateTimeField(auto_now_add=True)
