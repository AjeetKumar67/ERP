from django.test import TestCase
from .models import PerformanceReport, FinancialReport

class PerformanceReportTestCase(TestCase):
    def setUp(self):
        self.report = PerformanceReport.objects.create(
            student_id=1,
            subject='Mathematics',
            score=85,
            term='2023-1'
        )

    def test_performance_report_creation(self):
        self.assertEqual(self.report.student_id, 1)
        self.assertEqual(self.report.subject, 'Mathematics')
        self.assertEqual(self.report.score, 85)
        self.assertEqual(self.report.term, '2023-1')

class FinancialReportTestCase(TestCase):
    def setUp(self):
        self.financial_report = FinancialReport.objects.create(
            student_id=1,
            amount_due=1500,
            payment_status='Pending',
            term='2023-1'
        )

    def test_financial_report_creation(self):
        self.assertEqual(self.financial_report.student_id, 1)
        self.assertEqual(self.financial_report.amount_due, 1500)
        self.assertEqual(self.financial_report.payment_status, 'Pending')
        self.assertEqual(self.financial_report.term, '2023-1')