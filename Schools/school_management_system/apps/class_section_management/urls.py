from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassSectionViewSet, SectionViewSet, SubjectViewSet

# Initialize the router
router = DefaultRouter()

# Register viewsets with the router
router.register('class-sections', ClassSectionViewSet, basename='class-section')
router.register('sections', SectionViewSet, basename='section')
router.register('subjects', SubjectViewSet, basename='subject')

# Define urlpatterns
urlpatterns = [
    path('api/', include(router.urls)),  # Add a prefix like 'api/' for better API organization
]