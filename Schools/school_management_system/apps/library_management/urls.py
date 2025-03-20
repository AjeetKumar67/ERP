from django.urls import path
from .views import BookListView, IssueBookView, ReturnBookView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('issue/', IssueBookView.as_view(), name='issue-book'),
    path('return/', ReturnBookView.as_view(), name='return-book'),
]