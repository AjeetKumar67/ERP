from django.db import models

class PerformanceReport(models.Model):
    student = models.ForeignKey('student_management.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('class_section_management.Subject', on_delete=models.CASCADE)
    term = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.term} {self.year}"

class FinancialReport(models.Model):
    student = models.ForeignKey('student_management.Student', on_delete=models.CASCADE)
    fee_structure = models.ForeignKey('fee_accounting.FeeStructure', on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Due', 'Due')])
    report_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.fee_structure} - {self.payment_status}"