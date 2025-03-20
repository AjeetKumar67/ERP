from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Attendance
from django.utils import timezone
from django.views import View

class AttendanceView(View):
    def get(self, request):
        attendance_records = Attendance.objects.all()
        return render(request, 'attendance_management/attendance_list.html', {'attendance_records': attendance_records})

    def post(self, request):
        student_id = request.POST.get('student_id')
        status = request.POST.get('status')
        date = timezone.now().date()

        attendance_record, created = Attendance.objects.get_or_create(student_id=student_id, date=date)
        attendance_record.status = status
        attendance_record.save()

        return JsonResponse({'success': True})

class AttendanceDetailView(View):
    def get(self, request, student_id):
        attendance_records = Attendance.objects.filter(student_id=student_id)
        return render(request, 'attendance_management/attendance_detail.html', {'attendance_records': attendance_records})