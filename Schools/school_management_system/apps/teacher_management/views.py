from django.shortcuts import render, redirect
from django.views import View
from .models import Teacher, ClassSchedule, Leave
from .forms import TeacherForm, ClassScheduleForm, LeaveForm

class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, 'teacher_management/teacher_list.html', {'teachers': teachers})

class TeacherCreateView(View):
    def get(self, request):
        form = TeacherForm()
        return render(request, 'teacher_management/teacher_form.html', {'form': form})

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        return render(request, 'teacher_management/teacher_form.html', {'form': form})

class TeacherUpdateView(View):
    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        form = TeacherForm(instance=teacher)
        return render(request, 'teacher_management/teacher_form.html', {'form': form})

    def post(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        return render(request, 'teacher_management/teacher_form.html', {'form': form})

class TeacherDeleteView(View):
    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return redirect('teacher_list')

class ClassScheduleView(View):
    def get(self, request):
        schedules = ClassSchedule.objects.all()
        return render(request, 'teacher_management/class_schedule.html', {'schedules': schedules})

class ClassScheduleCreateView(View):
    def get(self, request):
        form = ClassScheduleForm()
        return render(request, 'teacher_management/class_schedule_form.html', {'form': form})

    def post(self, request):
        form = ClassScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_schedule')
        return render(request, 'teacher_management/class_schedule_form.html', {'form': form})

class LeaveRequestView(View):
    def get(self, request):
        leaves = Leave.objects.all()
        return render(request, 'teacher_management/leave_request.html', {'leaves': leaves})

class LeaveRequestCreateView(View):
    def get(self, request):
        form = LeaveForm()
        return render(request, 'teacher_management/leave_form.html', {'form': form})

    def post(self, request):
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_request')
        return render(request, 'teacher_management/leave_form.html', {'form': form})