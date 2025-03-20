from django.test import TestCase
from .models import Timetable, Schedule

class TimetableModelTests(TestCase):

    def setUp(self):
        self.timetable = Timetable.objects.create(
            class_name='10A',
            subject='Mathematics',
            teacher='Mr. Smith',
            day='Monday',
            start_time='09:00',
            end_time='10:00'
        )

    def test_timetable_creation(self):
        self.assertEqual(self.timetable.class_name, '10A')
        self.assertEqual(self.timetable.subject, 'Mathematics')
        self.assertEqual(self.timetable.teacher, 'Mr. Smith')
        self.assertEqual(self.timetable.day, 'Monday')
        self.assertEqual(self.timetable.start_time, '09:00')
        self.assertEqual(self.timetable.end_time, '10:00')

class ScheduleModelTests(TestCase):

    def setUp(self):
        self.schedule = Schedule.objects.create(
            timetable=self.timetable,
            week='Week 1',
            notes='Math class for revision'
        )

    def test_schedule_creation(self):
        self.assertEqual(self.schedule.timetable, self.timetable)
        self.assertEqual(self.schedule.week, 'Week 1')
        self.assertEqual(self.schedule.notes, 'Math class for revision')