# from django.contrib import admin
# from .models import Student, Admission, Attendance

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name')  # Replace 'name' with 'first_name' and 'last_name'
#     search_fields = ('name',)
#     list_filter = ('date_of_birth',)  # Replace 'class_section' with a valid field

# @admin.register(Admission)
# class AdmissionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'student', 'date_of_admission')  # Replace 'admission_date' with 'date_of_admission' or a valid field
#     search_fields = ('student__name',)
#     list_filter = ('date_of_admission',)  # Replace 'admission_date' with a valid field

# @admin.register(Attendance)
# class AttendanceAdmin(admin.ModelAdmin):
#     list_display = ('student', 'date', 'status')
#     search_fields = ('student__first_name', 'student__last_name')
#     list_filter = ('status',)