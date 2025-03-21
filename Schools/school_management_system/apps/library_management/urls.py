from django.urls import path
from .views import (
    BookListView, BookDetailView,
    CatalogListView, CatalogDetailView,
    FineListView, FineDetailView
)

urlpatterns = [
    # Book URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Catalog URLs
    path('catalogs/', CatalogListView.as_view(), name='catalog-list'),
    path('catalogs/<int:pk>/', CatalogDetailView.as_view(), name='catalog-detail'),

    # Fine URLs
    path('fines/', FineListView.as_view(), name='fine-list'),
    path('fines/<int:pk>/', FineDetailView.as_view(), name='fine-detail'),
]