from rest_framework import serializers
from .models import PerformanceReport, FinancialReport

class PerformanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReport
        fields = [
            'id',
            'student',
            'subject',
            'term',
            'year',
            'marks_obtained',
            'total_marks',
            'grade'
        ]

class FinancialReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialReport
        fields = [
            'id',
            'student',
            'fee_structure',
            'amount_due',
            'amount_paid',
            'payment_status',
            'report_date'
        ]