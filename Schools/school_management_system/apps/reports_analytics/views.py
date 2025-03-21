from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import PerformanceReport, FinancialReport
from .serializers import PerformanceReportSerializer, FinancialReportSerializer

class PerformanceReportView(APIView):
    def get(self, request):
        reports = PerformanceReport.objects.all()
        serializer = PerformanceReportSerializer(reports, many=True)
        return render(request, 'reports_analytics/performance_report.html', {'reports': serializer.data})

class FinancialReportView(APIView):
    def get(self, request):
        reports = FinancialReport.objects.all()
        serializer = FinancialReportSerializer(reports, many=True)
        return render(request, 'reports_analytics/financial_report.html', {'reports': serializer.data})

class GeneratePerformanceReportView(APIView):
    def get(self, request, student_id):
        report = PerformanceReport.objects.filter(student_id=student_id).first()
        if report:
            serializer = PerformanceReportSerializer(report)
            return Response({'status': 'success', 'data': serializer.data})
        return Response({'status': 'error', 'message': 'Report not found'})

class GenerateFinancialReportView(APIView):
    def get(self, request, student_id):
        report = FinancialReport.objects.filter(student_id=student_id).first()
        if report:
            serializer = FinancialReportSerializer(report)
            return Response({'status': 'success', 'data': serializer.data})
        return Response({'status': 'error', 'message': 'Report not found'})