from django.test import TestCase
from .models import Exam, Marks, ReportCard

class ExamModelTest(TestCase):
    def setUp(self):
        self.exam = Exam.objects.create(name="Midterm Exam", date="2023-10-15")

    def test_exam_creation(self):
        self.assertEqual(self.exam.name, "Midterm Exam")
        self.assertEqual(str(self.exam.date), "2023-10-15")

class MarksModelTest(TestCase):
    def setUp(self):
        self.exam = Exam.objects.create(name="Final Exam", date="2023-12-15")
        self.marks = Marks.objects.create(exam=self.exam, student_id=1, score=85)

    def test_marks_creation(self):
        self.assertEqual(self.marks.score, 85)
        self.assertEqual(self.marks.exam.name, "Final Exam")

class ReportCardModelTest(TestCase):
    def setUp(self):
        self.exam = Exam.objects.create(name="Midterm Exam", date="2023-10-15")
        self.report_card = ReportCard.objects.create(student_id=1, exam=self.exam, grade="A")

    def test_report_card_creation(self):
        self.assertEqual(self.report_card.grade, "A")
        self.assertEqual(self.report_card.exam.name, "Midterm Exam")