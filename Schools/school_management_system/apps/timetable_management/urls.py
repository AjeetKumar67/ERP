from django.urls import path
from .views import TimetableListView, GenerateTimetableView

urlpatterns = [
    path('', TimetableListView.as_view(), name='timetable-list'),
    path('generate/', GenerateTimetableView.as_view(), name='generate-timetable'),
]