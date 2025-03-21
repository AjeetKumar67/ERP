from django.urls import path
from .views import NotificationListView, MessageListView, SendMessageView, NotificationCreateView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('send-message/', SendMessageView.as_view(), name='send-message'),
    path('create-notification/', NotificationCreateView.as_view(), name='create-notification'),
]