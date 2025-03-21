from django.urls import path
from .views import (
    RoomListCreateView,
    AllocateRoomView,
    ViewAllocationsView,
    MarkAttendanceView,
    ViewAttendanceView,
)

urlpatterns = [
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('allocate-room/', AllocateRoomView.as_view(), name='allocate-room'),
    path('view-allocations/', ViewAllocationsView.as_view(), name='view-allocations'),
    path('mark-attendance/', MarkAttendanceView.as_view(), name='mark-attendance'),
    path('view-attendance/', ViewAttendanceView.as_view(), name='view-attendance'),
]