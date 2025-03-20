from django.urls import path
from .views import APIKeySettingsView, SystemSettingsView

urlpatterns = [
    path('api-keys/', APIKeySettingsView.as_view(), name='api-key-settings'),
    path('system/', SystemSettingsView.as_view(), name='system-settings'),
]