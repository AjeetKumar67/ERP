from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CollegeViewSet, DepartmentViewSet, FacultyViewSet, StudentViewSet, HostelViewSet,
    HostelRoomViewSet, HostelAllocationViewSet, LibraryViewSet, BookViewSet, BookIssueViewSet,
    CourseViewSet, CourseEnrollmentViewSet, AttendanceViewSet, ExaminationViewSet, ExamResultViewSet,
    FeeViewSet, EventViewSet, NoticeViewSet, AcademicYearViewSet, SemesterViewSet, SyllabusViewSet,
    AssignmentViewSet, AssignmentSubmissionViewSet, StudentAttendanceSummaryViewSet, TimeTableViewSet,
    GradeSystemViewSet, StudentGradeViewSet, PaymentTransactionViewSet
)

router = DefaultRouter()
router.register(r'colleges', CollegeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'faculties', FacultyViewSet)
router.register(r'students', StudentViewSet)
router.register(r'hostels', HostelViewSet)
router.register(r'hostel-rooms', HostelRoomViewSet)
router.register(r'hostel-allocations', HostelAllocationViewSet)
router.register(r'libraries', LibraryViewSet)
router.register(r'books', BookViewSet)
router.register(r'book-issues', BookIssueViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'course-enrollments', CourseEnrollmentViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'examinations', ExaminationViewSet)
router.register(r'exam-results', ExamResultViewSet)
router.register(r'fees', FeeViewSet)
router.register(r'events', EventViewSet)
router.register(r'notices', NoticeViewSet)
router.register(r'academic-years', AcademicYearViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'syllabi', SyllabusViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'assignment-submissions', AssignmentSubmissionViewSet)
router.register(r'student-attendance-summaries', StudentAttendanceSummaryViewSet)
router.register(r'time-tables', TimeTableViewSet)
router.register(r'grade-systems', GradeSystemViewSet)
router.register(r'student-grades', StudentGradeViewSet)
router.register(r'payment-transactions', PaymentTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
