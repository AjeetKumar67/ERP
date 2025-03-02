from django.db import models
from User.models import User

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=100)
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='reports/')
