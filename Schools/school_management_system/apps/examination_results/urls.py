from django.urls import path
from .views import ExamListView, MarksEntryView, ReportCardView

urlpatterns = [
    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('marks-entry/', MarksEntryView.as_view(), name='marks-entry'),
    path('report-card/', ReportCardView.as_view(), name='report-card'),
]