from django.urls import path
from .views import (
    SupplyListView,
    SupplyDetailView,
    UniformListView,
    UniformDetailView,
)

urlpatterns = [
    path('supplies/', SupplyListView.as_view(), name='supply-list'),
    path('supplies/<int:pk>/', SupplyDetailView.as_view(), name='supply-detail'),
    path('uniforms/', UniformListView.as_view(), name='uniform-list'),
    path('uniforms/<int:pk>/', UniformDetailView.as_view(), name='uniform-detail'),
]