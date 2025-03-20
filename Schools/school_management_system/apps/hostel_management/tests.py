from django.test import TestCase
from .models import RoomAllocation, Attendance

class RoomAllocationModelTest(TestCase):
    def setUp(self):
        self.allocation = RoomAllocation.objects.create(
            student_name="John Doe",
            room_number="101",
            check_in_date="2023-01-01",
            check_out_date="2023-06-01"
        )

    def test_room_allocation_str(self):
        self.assertEqual(str(self.allocation), "John Doe - Room 101")

class AttendanceModelTest(TestCase):
    def setUp(self):
        self.attendance = Attendance.objects.create(
            student_name="Jane Doe",
            date="2023-01-01",
            status="Present"
        )

    def test_attendance_str(self):
        self.assertEqual(str(self.attendance), "Jane Doe - Present on 2023-01-01")