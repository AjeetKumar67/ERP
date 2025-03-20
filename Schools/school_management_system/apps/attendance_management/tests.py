from django.test import TestCase
from .models import Attendance, Student

class AttendanceModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            roll_number='12345'
        )
        self.attendance = Attendance.objects.create(
            student=self.student,
            date='2023-10-01',
            status='Present'
        )

    def test_attendance_creation(self):
        self.assertEqual(self.attendance.student, self.student)
        self.assertEqual(self.attendance.date, '2023-10-01')
        self.assertEqual(self.attendance.status, 'Present')

    def test_attendance_str(self):
        self.assertEqual(str(self.attendance), f'{self.student} - {self.attendance.date}')

    def test_attendance_status(self):
        self.attendance.status = 'Absent'
        self.attendance.save()
        self.assertEqual(self.attendance.status, 'Absent')