from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Catalog(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.book.title} - {self.location}"

class Fine(models.Model):
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateField()
    due_date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Fine for {self.book.title} by {self.user.username}"