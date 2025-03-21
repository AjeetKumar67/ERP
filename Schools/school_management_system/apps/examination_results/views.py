from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import Exam, Marks, ReportCard
from .serializers import ExamSerializer, MarksSerializer, ReportCardSerializer

class ExamListView(APIView):
    def get(self, request):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

class ExamDetailView(APIView):
    def get(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        serializer = ExamSerializer(exam)
        return Response(serializer.data)

class MarksListView(APIView):
    def get(self, request):
        marks = Marks.objects.all()
        serializer = MarksSerializer(marks, many=True)
        return Response(serializer.data)

class ReportCardView(APIView):
    def get(self, request, student_id):
        report_card = get_object_or_404(ReportCard, student_id=student_id)
        serializer = ReportCardSerializer(report_card)
        return Response(serializer.data)

class GenerateReportCardView(APIView):
    def post(self, request, student_id):
        # Logic to generate report card
        report_card = ReportCard.objects.create(student_id=student_id)
        serializer = ReportCardSerializer(report_card)
        return Response({'status': 'success', 'report_card': serializer.data}, status=status.HTTP_201_CREATED)