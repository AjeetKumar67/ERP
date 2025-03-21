from django.urls import path
from .views import (
    ExamListView,
    ExamDetailView,
    MarksListView,
    ReportCardView,
    GenerateReportCardView
)

urlpatterns = [
    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('marks/', MarksListView.as_view(), name='marks-list'),
    path('report-card/<int:student_id>/', ReportCardView.as_view(), name='report-card'),
    path('generate-report-card/<int:student_id>/', GenerateReportCardView.as_view(), name='generate-report-card'),
]