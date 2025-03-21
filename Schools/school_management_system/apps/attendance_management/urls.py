from django.urls import path
from .views import AttendanceView, AttendanceDetailView, BiometricView

urlpatterns = [
    path('api/attendance/', AttendanceView.as_view(), name='attendance-api'),
    path('api/attendance/<int:student_id>/', AttendanceDetailView.as_view(), name='attendance-detail-api'),
    path('api/biometric/', BiometricView.as_view(), name='biometric-api'),
]
