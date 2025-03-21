from django.urls import path
from .views import (
    TimetableListView,
    TimetableDetailView,
    ScheduleListView,
    ScheduleDetailView
)

urlpatterns = [
    path('timetables/', TimetableListView.as_view(), name='timetable-list'),
    path('timetables/<int:pk>/', TimetableDetailView.as_view(), name='timetable-detail'),
    path('schedules/', ScheduleListView.as_view(), name='schedule-list'),
    path('schedules/<int:pk>/', ScheduleDetailView.as_view(), name='schedule-detail'),
]