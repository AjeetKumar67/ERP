# from django.contrib import admin
# from .models import PerformanceReport, FinancialReport

# @admin.register(PerformanceReport)
# class PerformanceReportAdmin(admin.ModelAdmin):
#     list_display = ('student', 'subject', 'grade', 'term', 'created_at')
#     search_fields = ('student__name', 'subject__name')
#     list_filter = ('term',)

# @admin.register(FinancialReport)
# class FinancialReportAdmin(admin.ModelAdmin):
#     list_display = ('id', 'report_name', 'generated_date')  # Replace invalid fields
#     list_filter = ('generated_date',)  # Replace 'due_date' with a valid field