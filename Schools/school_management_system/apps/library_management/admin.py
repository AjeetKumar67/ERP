from django.contrib import admin
from .models import Book, Catalog, Fine

admin.site.register(Book)
admin.site.register(Catalog)
admin.site.register(Fine)