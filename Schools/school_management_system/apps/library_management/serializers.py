from rest_framework import serializers
from .models import Book, Catalog, Fine

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'isbn', 'published_date',
            'category', 'quantity', 'available_copies'
        ]

class CatalogSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Catalog
        fields = ['id', 'book', 'added_date', 'location']

class FineSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Fine
        fields = [
            'id', 'user', 'book', 'fine_amount', 'issued_date',
            'due_date', 'paid'
        ]