from rest_framework import generics
from .models import Book, Catalog, Fine
from .serializers import BookSerializer, CatalogSerializer, FineSerializer

# Book Views
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Catalog Views
class CatalogListView(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class CatalogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

# Fine Views
class FineListView(generics.ListCreateAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer

class FineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
