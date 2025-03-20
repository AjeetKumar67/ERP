from django.urls import path
from .views import AttendanceListView, MarkAttendanceView

urlpatterns = [
    path('', AttendanceListView.as_view(), name='attendance-list'),
    path('mark/', MarkAttendanceView.as_view(), name='mark-attendance'),
]