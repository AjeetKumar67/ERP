from django.urls import path
from .views import (
    ClassSessionListView,
    ClassSessionDetailView,
    AssignmentListView,
    AssignmentDetailView,
    CreateClassSessionView,
    CreateAssignmentView,
    JoinClassSessionView,
    SubmitAssignmentView,
)

urlpatterns = [
    path('classes/', ClassSessionListView.as_view(), name='class-session-list'),
    path('classes/<int:pk>/', ClassSessionDetailView.as_view(), name='class-session-detail'),
    path('classes/create/', CreateClassSessionView.as_view(), name='create-class-session'),
    path('classes/<int:pk>/join/', JoinClassSessionView.as_view(), name='join-class-session'),
    path('assignments/', AssignmentListView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('assignments/create/', CreateAssignmentView.as_view(), name='create-assignment'),
    path('assignments/<int:pk>/submit/', SubmitAssignmentView.as_view(), name='submit-assignment'),
]