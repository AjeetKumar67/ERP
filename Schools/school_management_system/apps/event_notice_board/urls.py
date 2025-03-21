from django.urls import path
from .views import (
    EventListCreateView,
    EventDetailView,
    AnnouncementListCreateView,
    AnnouncementDetailView,
)

urlpatterns = [
    # Event URLs
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),

    # Announcement URLs
    path('announcements/', AnnouncementListCreateView.as_view(), name='announcement-list-create'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement-detail'),
]