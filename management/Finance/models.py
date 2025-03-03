from django.db import models

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('bank', 'Bank'),
        ('cash', 'Cash'),
        ('payable', 'Payable'),
        ('receivable', 'Receivable'),
    ]
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('payment', 'Payment'),
        ('receipt', 'Receipt'),
        ('adjustment', 'Adjustment'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    client = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_number

class Tax(models.Model):
    TAX_TYPES = [
        ('vat', 'VAT'),
        ('gst', 'GST'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    tax_type = models.CharField(max_length=20, choices=TAX_TYPES)
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Budget(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class FinancialReport(models.Model):
    REPORT_TYPES = [
        ('balance_sheet', 'Balance Sheet'),
        ('profit_loss', 'Profit & Loss'),
        ('cash_flow', 'Cash Flow'),
    ]
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    generated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.report_type} - {self.generated_at}"
