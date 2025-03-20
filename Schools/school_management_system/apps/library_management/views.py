from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book, Catalog, Fine
from .forms import BookForm, CatalogForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_management/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library_management/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('library_management:book_list'))
    else:
        form = BookForm()
    return render(request, 'library_management/add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('library_management:book_detail', args=[book.id]))
    else:
        form = BookForm(instance=book)
    return render(request, 'library_management/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return HttpResponseRedirect(reverse('library_management:book_list'))
    return render(request, 'library_management/delete_book.html', {'book': book})

def catalog_list(request):
    catalogs = Catalog.objects.all()
    return render(request, 'library_management/catalog_list.html', {'catalogs': catalogs})

def add_catalog(request):
    if request.method == 'POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('library_management:catalog_list'))
    else:
        form = CatalogForm()
    return render(request, 'library_management/add_catalog.html', {'form': form})

def fine_list(request):
    fines = Fine.objects.all()
    return render(request, 'library_management/fine_list.html', {'fines': fines})