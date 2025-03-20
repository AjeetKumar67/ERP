from django.test import TestCase
from .models import Book, Catalog, Fine

class LibraryManagementTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(title="Test Book", author="Test Author", isbn="1234567890123")
        self.catalog = Catalog.objects.create(book=self.book, available_copies=5)
        self.fine = Fine.objects.create(book=self.book, amount=10.00)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_catalog_creation(self):
        self.assertEqual(self.catalog.book, self.book)
        self.assertEqual(self.catalog.available_copies, 5)

    def test_fine_creation(self):
        self.assertEqual(self.fine.book, self.book)
        self.assertEqual(self.fine.amount, 10.00)

    def test_book_availability(self):
        self.assertTrue(self.catalog.available_copies > 0)

    def test_fine_amount(self):
        self.assertGreater(self.fine.amount, 0)