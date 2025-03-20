from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Timetable, Schedule
from django.views import View
from django.utils import timezone

class TimetableView(View):
    def get(self, request):
        timetables = Timetable.objects.all()
        return render(request, 'timetable_management/timetable_list.html', {'timetables': timetables})

class TimetableDetailView(View):
    def get(self, request, pk):
        timetable = Timetable.objects.get(pk=pk)
        return render(request, 'timetable_management/timetable_detail.html', {'timetable': timetable})

class TimetableCreateView(View):
    def get(self, request):
        return render(request, 'timetable_management/timetable_form.html')

    def post(self, request):
        timetable = Timetable()
        timetable.name = request.POST['name']
        timetable.created_at = timezone.now()
        timetable.save()
        return redirect('timetable_list')

class TimetableUpdateView(View):
    def get(self, request, pk):
        timetable = Timetable.objects.get(pk=pk)
        return render(request, 'timetable_management/timetable_form.html', {'timetable': timetable})

    def post(self, request, pk):
        timetable = Timetable.objects.get(pk=pk)
        timetable.name = request.POST['name']
        timetable.save()
        return redirect('timetable_list')

class TimetableDeleteView(View):
    def post(self, request, pk):
        timetable = Timetable.objects.get(pk=pk)
        timetable.delete()
        return redirect('timetable_list')

class ScheduleView(View):
    def get(self, request):
        schedules = Schedule.objects.all()
        return render(request, 'timetable_management/schedule_list.html', {'schedules': schedules})

class ScheduleCreateView(View):
    def get(self, request):
        return render(request, 'timetable_management/schedule_form.html')

    def post(self, request):
        schedule = Schedule()
        schedule.class_name = request.POST['class_name']
        schedule.subject = request.POST['subject']
        schedule.day = request.POST['day']
        schedule.start_time = request.POST['start_time']
        schedule.end_time = request.POST['end_time']
        schedule.save()
        return redirect('schedule_list')

class ScheduleUpdateView(View):
    def get(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        return render(request, 'timetable_management/schedule_form.html', {'schedule': schedule})

    def post(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        schedule.class_name = request.POST['class_name']
        schedule.subject = request.POST['subject']
        schedule.day = request.POST['day']
        schedule.start_time = request.POST['start_time']
        schedule.end_time = request.POST['end_time']
        schedule.save()
        return redirect('schedule_list')

class ScheduleDeleteView(View):
    def post(self, request, pk):
        schedule = Schedule.objects.get(pk=pk)
        schedule.delete()
        return redirect('schedule_list')