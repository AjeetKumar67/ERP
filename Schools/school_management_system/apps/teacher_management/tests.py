from django.test import TestCase
from .models import Teacher, ClassSchedule, Leave

class TeacherModelTests(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(
            first_name='John',
            last_name='Doe',
            subject='Mathematics',
            email='john.doe@example.com'
        )

    def test_teacher_creation(self):
        self.assertEqual(self.teacher.first_name, 'John')
        self.assertEqual(self.teacher.last_name, 'Doe')
        self.assertEqual(self.teacher.subject, 'Mathematics')
        self.assertEqual(self.teacher.email, 'john.doe@example.com')

class ClassScheduleModelTests(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(
            first_name='Jane',
            last_name='Smith',
            subject='Science',
            email='jane.smith@example.com'
        )
        self.schedule = ClassSchedule.objects.create(
            teacher=self.teacher,
            class_name='10A',
            day='Monday',
            time='09:00-10:00'
        )

    def test_class_schedule_creation(self):
        self.assertEqual(self.schedule.class_name, '10A')
        self.assertEqual(self.schedule.day, 'Monday')
        self.assertEqual(self.schedule.time, '09:00-10:00')

class LeaveModelTests(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(
            first_name='Alice',
            last_name='Johnson',
            subject='History',
            email='alice.johnson@example.com'
        )
        self.leave = Leave.objects.create(
            teacher=self.teacher,
            start_date='2023-10-01',
            end_date='2023-10-05',
            reason='Medical Leave'
        )

    def test_leave_creation(self):
        self.assertEqual(self.leave.reason, 'Medical Leave')
        self.assertEqual(self.leave.start_date, '2023-10-01')
        self.assertEqual(self.leave.end_date, '2023-10-05')