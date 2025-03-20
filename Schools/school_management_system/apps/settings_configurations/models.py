from django.db import models

class SystemSetting(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.key

class APIKey(models.Model):
    service_name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name

class NotificationSetting(models.Model):
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)
    push_notifications = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification settings for {self.user.username}"