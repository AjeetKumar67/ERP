from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal



class College(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    established_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='departments')
    hod = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True, related_name='hod_department')
    
    def __str__(self):
        return f"{self.name} - {self.college.name}"


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculties')
    employee_id = models.CharField(max_length=20, unique=True)
    qualification = models.CharField(max_length=100)
    date_joined = models.DateField()
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.employee_id}"


class Student(models.Model):
    YEAR_CHOICES = [
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.registration_number}"


class Hostel(models.Model):
    HOSTEL_TYPES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    name = models.CharField(max_length=100)
    hostel_type = models.CharField(max_length=1, choices=HOSTEL_TYPES)
    total_rooms = models.IntegerField()
    warden = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name


class HostelRoom(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.hostel.name} - Room {self.room_number}"


class HostelAllocation(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(HostelRoom, on_delete=models.CASCADE)
    allocated_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.room}"


class Library(models.Model):
    name = models.CharField(max_length=100)
    librarian = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    total_books = models.IntegerField()
    
    def __str__(self):
        return self.name


class Book(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.IntegerField()
    copies_available = models.IntegerField()
    
    def __str__(self):
        return self.title


class BookIssue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    is_returned = models.BooleanField(default=False)
    actual_return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.book.title} - {self.student.user.get_full_name()}"
    




class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    credits = models.IntegerField()
    description = models.TextField()
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.code} - {self.name}"


class CourseEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()
    enrollment_date = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ['student', 'course', 'semester']


class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['course', 'student', 'date']


class Examination(models.Model):
    EXAM_TYPES = [
        ('MID', 'Mid Term'),
        ('END', 'End Term'),
        ('QUIZ', 'Quiz'),
        ('ASSG', 'Assignment')
    ]
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=4, choices=EXAM_TYPES)
    date = models.DateTimeField()
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.course.code} - {self.exam_type}"


class ExamResult(models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        unique_together = ['examination', 'student']


class Fee(models.Model):
    FEE_TYPES = [
        ('TUT', 'Tuition'),
        ('HOS', 'Hostel'),
        ('LIB', 'Library'),
        ('LAB', 'Laboratory')
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=3, choices=FEE_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.student.registration_number} - {self.fee_type}"


class Event(models.Model):
    EVENT_TYPES = [
        ('CONF', 'Conference'),
        ('WORK', 'Workshop'),
        ('CULT', 'Cultural'),
        ('TECH', 'Technical'),
        ('SPRT', 'Sports')
    ]
    
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=4, choices=EVENT_TYPES)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    coordinator = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title


class Notice(models.Model):
    NOTICE_TYPES = [
        ('GEN', 'General'),
        ('EXAM', 'Examination'),
        ('DEPT', 'Department'),
        ('PLAC', 'Placement')
    ]
    
    title = models.CharField(max_length=200)
    notice_type = models.CharField(max_length=4, choices=NOTICE_TYPES)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    

# Add these imports at the top
# from django.core.validators import MinValueValidator, MaxValueValidator
# from decimal import Decimal

class AcademicYear(models.Model):
    year = models.CharField(max_length=9)  # e.g., "2024-2025"
    is_active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.year

class Semester(models.Model):
    SEMESTER_CHOICES = [
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Fifth'),
        (6, 'Sixth'),
        (7, 'Seventh'),
        (8, 'Eighth')
    ]
    
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    semester_number = models.IntegerField(choices=SEMESTER_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta:
        unique_together = ['academic_year', 'semester_number']

class Syllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='syllabi')
    title = models.CharField(max_length=200)
    content = models.TextField()
    version = models.CharField(max_length=20)
    effective_from = models.DateField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "syllabi"

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
    file_attachment = models.FileField(upload_to='assignments/', null=True, blank=True)

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    file_submission = models.FileField(upload_to='submissions/')
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    remarks = models.TextField(blank=True)

class StudentAttendanceSummary(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    total_classes = models.IntegerField(default=0)
    classes_attended = models.IntegerField(default=0)
    attendance_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        unique_together = ['student', 'course', 'semester']

class TimeTable(models.Model):
    DAYS_OF_WEEK = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday')
    ]
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.CharField(max_length=50)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['day', 'start_time', 'room_number', 'semester']

class GradeSystem(models.Model):
    grade = models.CharField(max_length=2)  # A+, A, B+, etc.
    min_marks = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2)
    grade_point = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self):
        return f"{self.grade} ({self.min_marks}-{self.max_marks})"

class StudentGrade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    grade = models.ForeignKey(GradeSystem, on_delete=models.PROTECT)
    cgpa = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    class Meta:
        unique_together = ['student', 'course', 'semester']

class PaymentTransaction(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('CARD', 'Card'),
        ('UPI', 'UPI'),
        ('NET', 'Net Banking'),
    ]
    
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=4, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20)  # success, pending, failed
    remarks = models.TextField(blank=True)