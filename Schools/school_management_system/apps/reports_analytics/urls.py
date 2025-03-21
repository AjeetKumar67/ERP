from django.urls import path
from .views import (
    PerformanceReportView,
    FinancialReportView,
    GeneratePerformanceReportView,
    GenerateFinancialReportView,
)

urlpatterns = [
    path('performance-report/', PerformanceReportView.as_view(), name='performance-report'),
    path('financial-report/', FinancialReportView.as_view(), name='financial-report'),
    path('generate-performance-report/<int:student_id>/', GeneratePerformanceReportView.as_view(), name='generate-performance-report'),
    path('generate-financial-report/<int:student_id>/', GenerateFinancialReportView.as_view(), name='generate-financial-report'),
]
