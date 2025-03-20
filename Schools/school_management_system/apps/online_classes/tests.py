from django.test import TestCase
from .models import ClassSession, Assignment

class ClassSessionModelTest(TestCase):
    def setUp(self):
        self.session = ClassSession.objects.create(
            title="Math Class",
            description="Online Math Class",
            scheduled_time="2023-10-01T10:00:00Z",
            duration=60
        )

    def test_class_session_creation(self):
        self.assertEqual(self.session.title, "Math Class")
        self.assertEqual(self.session.description, "Online Math Class")
        self.assertEqual(self.session.duration, 60)

class AssignmentModelTest(TestCase):
    def setUp(self):
        self.assignment = Assignment.objects.create(
            title="Math Homework",
            description="Complete exercises 1 to 10",
            due_date="2023-10-05",
            class_session=self.session
        )

    def test_assignment_creation(self):
        self.assertEqual(self.assignment.title, "Math Homework")
        self.assertEqual(self.assignment.description, "Complete exercises 1 to 10")
        self.assertEqual(self.assignment.due_date, "2023-10-05")