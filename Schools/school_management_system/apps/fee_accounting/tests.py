from django.test import TestCase
from .models import FeeStructure, Payment, Invoice

class FeeAccountingTests(TestCase):

    def setUp(self):
        self.fee_structure = FeeStructure.objects.create(
            class_name='10th Grade',
            amount=1500,
            due_date='2023-09-30'
        )
        self.payment = Payment.objects.create(
            fee_structure=self.fee_structure,
            amount_paid=1500,
            payment_date='2023-09-15',
            payment_method='Online'
        )
        self.invoice = Invoice.objects.create(
            payment=self.payment,
            invoice_number='INV-001',
            issued_date='2023-09-16'
        )

    def test_fee_structure_creation(self):
        self.assertEqual(self.fee_structure.class_name, '10th Grade')
        self.assertEqual(self.fee_structure.amount, 1500)

    def test_payment_creation(self):
        self.assertEqual(self.payment.amount_paid, 1500)
        self.assertEqual(self.payment.payment_method, 'Online')

    def test_invoice_creation(self):
        self.assertEqual(self.invoice.invoice_number, 'INV-001')
        self.assertEqual(self.invoice.issued_date, '2023-09-16')

    def test_fee_structure_str(self):
        self.assertEqual(str(self.fee_structure), '10th Grade - 1500')

    def test_payment_str(self):
        self.assertEqual(str(self.payment), 'Payment of 1500 for 10th Grade')

    def test_invoice_str(self):
        self.assertEqual(str(self.invoice), 'Invoice INV-001 for Payment of 1500')