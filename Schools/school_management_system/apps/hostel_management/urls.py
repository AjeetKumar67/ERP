from django.urls import path
from .views import RoomAllocationView, HostelAttendanceView

urlpatterns = [
    path('room-allocation/', RoomAllocationView.as_view(), name='room-allocation'),
    path('attendance/', HostelAttendanceView.as_view(), name='hostel-attendance'),
]