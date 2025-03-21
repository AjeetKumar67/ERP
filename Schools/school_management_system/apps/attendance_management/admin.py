from django.contrib import admin
from .models import Attendance, Biometric

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    search_fields = ('student__name', 'date')
    list_filter = ('status', 'date')

@admin.register(Biometric)
class BiometricAdmin(admin.ModelAdmin):
    list_display = ('student', 'timestamp', 'status')  # Replace 'action' with 'status'
    search_fields = ('student__name', 'status')  # Replace 'action' with 'status'
    list_filter = ('status', 'timestamp')  # Replace 'action' with 'status'