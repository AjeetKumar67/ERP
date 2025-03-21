from django.urls import path

from .views import (
    TeacherListView,
    TeacherCreateView,
    TeacherUpdateView,
    TeacherDeleteView,
    ClassScheduleView,
    ClassScheduleCreateView,
    LeaveRequestView,
    LeaveRequestCreateView,
)

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher-create'),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher-update'),
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
    path('class-schedules/', ClassScheduleView.as_view(), name='class-schedule-list'),
    path('class-schedules/create/', ClassScheduleCreateView.as_view(), name='class-schedule-create'),
    path('leaves/', LeaveRequestView.as_view(), name='leave-request-list'),
    path('leaves/create/', LeaveRequestCreateView.as_view(), name='leave-request-create'),
]