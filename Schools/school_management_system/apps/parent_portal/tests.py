from django.test import TestCase
from .models import ChildProgress, PaymentAlert

class ChildProgressModelTest(TestCase):
    def setUp(self):
        self.child_progress = ChildProgress.objects.create(
            student_name="John Doe",
            progress_report="Excellent progress in all subjects.",
            term="Term 1"
        )

    def test_child_progress_creation(self):
        self.assertEqual(self.child_progress.student_name, "John Doe")
        self.assertEqual(self.child_progress.progress_report, "Excellent progress in all subjects.")
        self.assertEqual(self.child_progress.term, "Term 1")

class PaymentAlertModelTest(TestCase):
    def setUp(self):
        self.payment_alert = PaymentAlert.objects.create(
            student_name="Jane Doe",
            amount_due=1500,
            due_date="2023-12-01"
        )

    def test_payment_alert_creation(self):
        self.assertEqual(self.payment_alert.student_name, "Jane Doe")
        self.assertEqual(self.payment_alert.amount_due, 1500)
        self.assertEqual(self.payment_alert.due_date, "2023-12-01")