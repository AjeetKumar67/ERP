from django.db import models
from django.contrib.auth.models import User

class ChildProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    progress_report = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child_name} - {self.grade}"

class PaymentAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment Alert for {self.user.username} - Amount Due: {self.amount_due}"