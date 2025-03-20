from django.contrib import admin
from .models import PerformanceReport, FinancialReport

@admin.register(PerformanceReport)
class PerformanceReportAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'term', 'created_at')
    search_fields = ('student__name', 'subject__name')
    list_filter = ('term',)

@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount_due', 'amount_paid', 'due_date', 'created_at')
    search_fields = ('student__name',)
    list_filter = ('due_date',)