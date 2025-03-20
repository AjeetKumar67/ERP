from django.shortcuts import render
from django.http import JsonResponse
from .models import PerformanceReport, FinancialReport

def performance_report(request):
    reports = PerformanceReport.objects.all()
    return render(request, 'reports_analytics/performance_report.html', {'reports': reports})

def financial_report(request):
    reports = FinancialReport.objects.all()
    return render(request, 'reports_analytics/financial_report.html', {'reports': reports})

def generate_performance_report(request, student_id):
    report = PerformanceReport.objects.filter(student_id=student_id).first()
    if report:
        return JsonResponse({'status': 'success', 'data': report.to_dict()})
    return JsonResponse({'status': 'error', 'message': 'Report not found'})

def generate_financial_report(request, student_id):
    report = FinancialReport.objects.filter(student_id=student_id).first()
    if report:
        return JsonResponse({'status': 'success', 'data': report.to_dict()})
    return JsonResponse({'status': 'error', 'message': 'Report not found'})