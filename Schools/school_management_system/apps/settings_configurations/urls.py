from django.urls import path
from .views import (
    APIKeySettingsView,
    SystemSettingsView,
    SettingsDashboardView,
    UpdateSettingView,
)

urlpatterns = [
    path('api-keys/', APIKeySettingsView.as_view(), name='api-key-settings'),
    path('system/', SystemSettingsView.as_view(), name='system-settings'),
    path('settings-dashboard/', SettingsDashboardView.as_view(), name='settings-dashboard'),
    path('update-setting/<int:setting_id>/', UpdateSettingView.as_view(), name='update-setting'),
]