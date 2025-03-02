from django.shortcuts import render
from rest_framework import generics
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

# Create your views here.
