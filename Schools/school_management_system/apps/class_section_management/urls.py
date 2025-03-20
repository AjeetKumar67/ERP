from django.urls import path
from .views import ClassListView, SectionListView, AssignTeacherView

urlpatterns = [
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('sections/', SectionListView.as_view(), name='section-list'),
    path('assign-teacher/', AssignTeacherView.as_view(), name='assign-teacher'),
]