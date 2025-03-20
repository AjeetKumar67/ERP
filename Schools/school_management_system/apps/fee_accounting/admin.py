from django.contrib import admin
from .models import FeeStructure, Payment, Invoice

admin.site.register(FeeStructure)
admin.site.register(Payment)
admin.site.register(Invoice)