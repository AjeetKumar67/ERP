# from django.urls import path
# from .views import StudentPerformanceReportView, FinancialAnalyticsView, AttendanceAnalyticsView

# urlpatterns = [
#     path('student-performance/', StudentPerformanceReportView.as_view(), name='student-performance-report'),
#     path('financial/', FinancialAnalyticsView.as_view(), name='financial-analytics'),
#     path('attendance/', AttendanceAnalyticsView.as_view(), name='attendance-analytics'),
# ]
from django.urls import path
from .views import StudentPerformanceReportView, FinancialAnalyticsView, AttendanceAnalyticsView

urlpatterns = [
    path('student-performance/', StudentPerformanceReportView.as_view(), name='student-performance-report'),
    path('financial/', FinancialAnalyticsView.as_view(), name='financial-analytics'),
    path('attendance/', AttendanceAnalyticsView.as_view(), name='attendance-analytics'),
]