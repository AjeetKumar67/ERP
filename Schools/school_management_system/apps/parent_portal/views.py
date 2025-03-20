from django.shortcuts import render
from django.views import View
from .models import ChildProgress, PaymentAlert

class ChildProgressView(View):
    def get(self, request):
        progress_records = ChildProgress.objects.all()
        return render(request, 'parent_portal/child_progress.html', {'progress_records': progress_records})

class PaymentAlertView(View):
    def get(self, request):
        alerts = PaymentAlert.objects.filter(is_active=True)
        return render(request, 'parent_portal/payment_alerts.html', {'alerts': alerts})