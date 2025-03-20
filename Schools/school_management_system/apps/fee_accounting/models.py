from django.db import models

class FeeStructure(models.Model):
    class Meta:
        verbose_name = "Fee Structure"
        verbose_name_plural = "Fee Structures"

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    student = models.ForeignKey('student_management.Student', on_delete=models.CASCADE)
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student} - {self.amount_paid} on {self.payment_date}"


class Invoice(models.Model):
    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50, unique=True)
    generated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.invoice_number