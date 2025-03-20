from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Attendance
from django.contrib import messages
from django.views import View

class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'student_management/student_list.html', {'students': students})

class StudentDetailView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        return render(request, 'student_management/student_detail.html', {'student': student})

class StudentCreateView(View):
    def get(self, request):
        return render(request, 'student_management/student_form.html')

    def post(self, request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        # Additional fields can be added here
        student = Student(name=name, age=age)
        student.save()
        messages.success(request, 'Student created successfully!')
        return redirect('student_list')

class StudentUpdateView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        return render(request, 'student_management/student_form.html', {'student': student})

    def post(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        # Update additional fields here
        student.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('student_list')

class StudentDeleteView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')

class AttendanceView(View):
    def get(self, request):
        attendance_records = Attendance.objects.all()
        return render(request, 'student_management/attendance_list.html', {'attendance_records': attendance_records})

    def post(self, request):
        student_id = request.POST.get('student_id')
        status = request.POST.get('status')
        attendance = Attendance(student_id=student_id, status=status)
        attendance.save()
        messages.success(request, 'Attendance recorded successfully!')
        return redirect('attendance_list')