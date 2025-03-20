from django.test import TestCase
from .models import Event, Announcement

class EventNoticeBoardTests(TestCase):

    def setUp(self):
        self.event = Event.objects.create(
            title="School Annual Day",
            description="Annual day celebration with performances.",
            date="2023-12-15",
            time="18:00",
            location="School Auditorium"
        )
        self.announcement = Announcement.objects.create(
            title="New Admission Open",
            content="Admissions for the new academic year are now open.",
            date="2023-10-01"
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, "School Annual Day")
        self.assertEqual(self.event.description, "Annual day celebration with performances.")
        self.assertEqual(str(self.event.date), "2023-12-15")
        self.assertEqual(self.event.time, "18:00")
        self.assertEqual(self.event.location, "School Auditorium")

    def test_announcement_creation(self):
        self.assertEqual(self.announcement.title, "New Admission Open")
        self.assertEqual(self.announcement.content, "Admissions for the new academic year are now open.")
        self.assertEqual(str(self.announcement.date), "2023-10-01")

    def test_event_str(self):
        self.assertEqual(str(self.event), "School Annual Day")

    def test_announcement_str(self):
        self.assertEqual(str(self.announcement), "New Admission Open")