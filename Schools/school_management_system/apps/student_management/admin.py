from django.contrib import admin
from .models import Student, Admission, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'enrollment_date', 'class_section')
    search_fields = ('first_name', 'last_name', 'class_section__name')
    list_filter = ('class_section',)

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'admission_date', 'status')
    search_fields = ('student__first_name', 'student__last_name')
    list_filter = ('status',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    search_fields = ('student__first_name', 'student__last_name')
    list_filter = ('status',)