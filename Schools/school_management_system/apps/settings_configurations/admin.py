from django.contrib import admin
from .models import SystemSetting, APIKey

@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'description')
    search_fields = ('key',)

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'key', 'created_at')
    search_fields = ('service_name',)