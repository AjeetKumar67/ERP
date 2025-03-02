from django.db import models
from management.Inventory.models import Product

# Create your models here.
class WorkOrder(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
