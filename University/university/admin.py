from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    College, Department, Faculty, Student,
    Hostel, HostelRoom, HostelAllocation,
    Library, Book, BookIssue, Course, CourseEnrollment, Attendance, Examination,
    ExamResult, Fee, Event, Notice, AcademicYear, Semester, Syllabus, Assignment, 
    AssignmentSubmission, StudentAttendanceSummary,
    TimeTable, GradeSystem, StudentGrade, PaymentTransaction
)

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'established_date', 'is_active')
    search_fields = ('name', 'code')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'college', 'hod')
    list_filter = ('college',)
    search_fields = ('name', 'code')

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'department', 'date_joined')
    search_fields = ('user__username', 'employee_id')
    list_filter = ('department',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'registration_number', 'department', 'year')
    search_fields = ('user__username', 'registration_number')
    list_filter = ('department', 'year')

@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ('name', 'hostel_type', 'total_rooms', 'warden')
    list_filter = ('hostel_type',)

@admin.register(HostelRoom)
class HostelRoomAdmin(admin.ModelAdmin):
    list_display = ('hostel', 'room_number', 'capacity', 'is_occupied')
    list_filter = ('hostel', 'is_occupied')

@admin.register(HostelAllocation)
class HostelAllocationAdmin(admin.ModelAdmin):
    list_display = ('student', 'room', 'allocated_date', 'is_active')
    list_filter = ('is_active',)

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'librarian', 'total_books')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'library', 'copies_available')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('library',)

@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = ('book', 'student', 'issue_date', 'return_date', 'is_returned', 'fine_amount')
    list_filter = ('is_returned',)
    search_fields = ('book__title', 'student__user__username')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'credits', 'faculty')
    search_fields = ('code', 'name')
    list_filter = ('department',)

@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'enrollment_date')
    list_filter = ('semester', 'course')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'date', 'is_present')
    list_filter = ('course', 'date', 'is_present')
    search_fields = ('student__user__username',)

@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    list_display = ('course', 'exam_type', 'date', 'total_marks')
    list_filter = ('exam_type', 'course')

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('examination', 'student', 'marks_obtained')
    search_fields = ('student__user__username',)

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'fee_type', 'amount', 'due_date', 'is_paid')
    list_filter = ('fee_type', 'is_paid')
    search_fields = ('student__user__username',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_date', 'end_date', 'venue')
    list_filter = ('event_type',)
    search_fields = ('title',)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'notice_type', 'publish_date', 'expiry_date')
    list_filter = ('notice_type', 'department')
    search_fields = ('title', 'content')



@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'is_active', 'start_date', 'end_date')
    list_filter = ('is_active',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('academic_year', 'semester_number', 'start_date', 'end_date')
    list_filter = ('academic_year', 'semester_number')

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'version', 'effective_from', 'is_active')
    list_filter = ('is_active', 'course')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'due_date', 'total_marks')
    list_filter = ('course',)
    search_fields = ('title',)

@admin.register(StudentAttendanceSummary)
class StudentAttendanceSummaryAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'attendance_percentage')
    list_filter = ('course', 'semester')

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('course', 'day', 'start_time', 'end_time', 'room_number')
    list_filter = ('day', 'semester')

@admin.register(GradeSystem)
class GradeSystemAdmin(admin.ModelAdmin):
    list_display = ('grade', 'min_marks', 'max_marks', 'grade_point')

@admin.register(StudentGrade)
class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'grade', 'cgpa')
    list_filter = ('semester', 'grade')

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ('fee', 'transaction_date', 'amount', 'payment_method', 'status')
    list_filter = ('payment_method', 'status')
    search_fields = ('transaction_id',)