from django.urls import path
from .views import FeeStructureView, PaymentView, InvoiceView

urlpatterns = [
    path('structure/', FeeStructureView.as_view(), name='fee-structure'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('invoice/', InvoiceView.as_view(), name='invoice'),
]