from rest_framework import serializers
from .models import SystemSetting, APIKey, NotificationSetting

class SystemSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetting
        fields = ['id', 'key', 'value', 'description']

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['id', 'service_name', 'api_key', 'created_at', 'updated_at']

class NotificationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSetting
        fields = ['id', 'user', 'email_notifications', 'sms_notifications', 'push_notifications']