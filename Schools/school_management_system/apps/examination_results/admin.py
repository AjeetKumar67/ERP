from django.contrib import admin
from .models import Exam, Marks, ReportCard

admin.site.register(Exam)
admin.site.register(Marks)
admin.site.register(ReportCard)