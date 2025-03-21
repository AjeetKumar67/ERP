from django.urls import path
from .views import ChildProgressAPIView, PaymentAlertAPIView

urlpatterns = [
    path('progress/', ChildProgressAPIView.as_view(), name='child-progress-api'),
    path('payment-alerts/', PaymentAlertAPIView.as_view(), name='payment-alerts-api'),
]
