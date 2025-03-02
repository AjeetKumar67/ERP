from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    client = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])
    created_at = models.DateTimeField(auto_now_add=True)

class Expense(models.Model):
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField()




# class Invoice(models.Model):
#     invoice_number = models.CharField(max_length=100, unique=True)
#     date_issued = models.DateField()
#     due_date = models.DateField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=50)

#     def __str__(self):
#         return self.invoice_number
