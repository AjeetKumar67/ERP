from django.urls import path
from .views import EventListView, NoticeListView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('notices/', NoticeListView.as_view(), name='notice-list'),
]