from django.urls import path
from .views import StudentListView, StudentDetailView, StudentAttendanceView

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('attendance/', StudentAttendanceView.as_view(), name='student-attendance'),
]