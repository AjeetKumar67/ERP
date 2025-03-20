from django.urls import path
from .views import InventoryListView, AddInventoryView, UpdateInventoryView

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory-list'),
    path('add/', AddInventoryView.as_view(), name='add-inventory'),
    path('update/<int:pk>/', UpdateInventoryView.as_view(), name='update-inventory'),
]