from django.test import TestCase
from .models import Class, Section, Subject

class ClassSectionManagementTests(TestCase):

    def setUp(self):
        self.class1 = Class.objects.create(name='10th Grade')
        self.section1 = Section.objects.create(name='A', class_assigned=self.class1)
        self.subject1 = Subject.objects.create(name='Mathematics', class_assigned=self.class1)

    def test_class_creation(self):
        self.assertEqual(self.class1.name, '10th Grade')

    def test_section_creation(self):
        self.assertEqual(self.section1.name, 'A')
        self.assertEqual(self.section1.class_assigned, self.class1)

    def test_subject_creation(self):
        self.assertEqual(self.subject1.name, 'Mathematics')
        self.assertEqual(self.subject1.class_assigned, self.class1)

    def test_class_str(self):
        self.assertEqual(str(self.class1), '10th Grade')

    def test_section_str(self):
        self.assertEqual(str(self.section1), 'A')

    def test_subject_str(self):
        self.assertEqual(str(self.subject1), 'Mathematics')