from django.urls import path
from .views import SendEmailView, SendSMSView, PushNotificationView

urlpatterns = [
    path('email/', SendEmailView.as_view(), name='send-email'),
    path('sms/', SendSMSView.as_view(), name='send-sms'),
    path('push-notification/', PushNotificationView.as_view(), name='push-notification'),
]