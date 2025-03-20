from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Exam, Marks, ReportCard
from django.views import View

class ExamListView(View):
    def get(self, request):
        exams = Exam.objects.all()
        return render(request, 'examination_results/exam_list.html', {'exams': exams})

class ExamDetailView(View):
    def get(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        return render(request, 'examination_results/exam_detail.html', {'exam': exam})

class MarksListView(View):
    def get(self, request):
        marks = Marks.objects.all()
        return render(request, 'examination_results/marks_list.html', {'marks': marks})

class ReportCardView(View):
    def get(self, request, student_id):
        report_card = get_object_or_404(ReportCard, student_id=student_id)
        return render(request, 'examination_results/report_card.html', {'report_card': report_card})

class GenerateReportCardView(View):
    def post(self, request, student_id):
        # Logic to generate report card
        report_card = ReportCard.objects.create(student_id=student_id)
        return JsonResponse({'status': 'success', 'report_card_id': report_card.id})