from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification, Message
from django.views import View

class NotificationListView(View):
    def get(self, request):
        notifications = Notification.objects.all()
        return render(request, 'communication_system/notification_list.html', {'notifications': notifications})

class MessageListView(View):
    def get(self, request):
        messages = Message.objects.all()
        return render(request, 'communication_system/message_list.html', {'messages': messages})

class SendMessageView(View):
    def post(self, request):
        recipient = request.POST.get('recipient')
        content = request.POST.get('content')
        message = Message.objects.create(recipient=recipient, content=content)
        return JsonResponse({'status': 'success', 'message_id': message.id})

class NotificationCreateView(View):
    def post(self, request):
        title = request.POST.get('title')
        message = request.POST.get('message')
        notification = Notification.objects.create(title=title, message=message)
        return JsonResponse({'status': 'success', 'notification_id': notification.id})