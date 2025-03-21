from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="School Management System API",
        default_version='v1',
        description="API documentation for the School Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@schoolmanagement.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.user_management.urls')),
    path('students/', include('apps.student_management.urls')),
    path('teachers/', include('apps.teacher_management.urls')),
    path('classes/', include('apps.class_section_management.urls')),
    path('timetable/', include('apps.timetable_management.urls')),
    path('attendance/', include('apps.attendance_management.urls')),
    path('exams/', include('apps.examination_results.urls')),
    path('fees/', include('apps.fee_accounting.urls')),
    path('library/', include('apps.library_management.urls')),
    path('transport/', include('apps.transport_management.urls')),
    path('hostel/', include('apps.hostel_management.urls')),
    path('parents/', include('apps.parent_portal.urls')),
    path('events/', include('apps.event_notice_board.urls')),
    path('online-classes/', include('apps.online_classes.urls')),
    path('communication/', include('apps.communication_system.urls')),
    path('inventory/', include('apps.inventory_management.urls')),
    path('reports/', include('apps.reports_analytics.urls')),
    path('settings/', include('apps.settings_configurations.urls')),

    # JWT Authentication URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]