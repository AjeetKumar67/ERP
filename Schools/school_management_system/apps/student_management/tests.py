from django.test import TestCase
from .models import Student, Admission, Attendance

class StudentModelTests(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='2005-05-15',
            admission_number='A12345'
        )
        self.assertEqual(student.first_name, 'John')
        self.assertEqual(student.last_name, 'Doe')
        self.assertEqual(student.admission_number, 'A12345')

class AdmissionModelTests(TestCase):

    def test_admission_process(self):
        admission = Admission.objects.create(
            student_id=1,
            admission_date='2023-01-10',
            status='Pending'
        )
        self.assertEqual(admission.status, 'Pending')

class AttendanceModelTests(TestCase):

    def test_attendance_record(self):
        attendance = Attendance.objects.create(
            student_id=1,
            date='2023-01-15',
            status='Present'
        )
        self.assertEqual(attendance.status, 'Present')