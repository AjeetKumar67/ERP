from django.contrib import admin
from django.urls import path, include

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
]