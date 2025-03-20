from django.urls import path
from .views import ChildProgressView, FeeAlertsView, AttendanceAlertsView

urlpatterns = [
    path('progress/', ChildProgressView.as_view(), name='child-progress'),
    path('fee-alerts/', FeeAlertsView.as_view(), name='fee-alerts'),
    path('attendance-alerts/', AttendanceAlertsView.as_view(), name='attendance-alerts'),
]