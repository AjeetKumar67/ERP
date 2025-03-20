from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RoomAllocation, HostelAttendance
from django.contrib.auth.decorators import login_required

@login_required
def allocate_room(request):
    if request.method == 'POST':
        # Logic for room allocation
        room_number = request.POST.get('room_number')
        student_id = request.POST.get('student_id')
        # Create RoomAllocation instance
        allocation = RoomAllocation(room_number=room_number, student_id=student_id)
        allocation.save()
        return redirect('room_allocation_success')
    return render(request, 'hostel_management/allocate_room.html')

@login_required
def view_allocations(request):
    allocations = RoomAllocation.objects.all()
    return render(request, 'hostel_management/view_allocations.html', {'allocations': allocations})

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        # Logic for marking attendance
        student_id = request.POST.get('student_id')
        date = request.POST.get('date')
        status = request.POST.get('status')
        attendance = HostelAttendance(student_id=student_id, date=date, status=status)
        attendance.save()
        return redirect('attendance_success')
    return render(request, 'hostel_management/mark_attendance.html')

@login_required
def view_attendance(request):
    attendance_records = HostelAttendance.objects.all()
    return render(request, 'hostel_management/view_attendance.html', {'attendance_records': attendance_records})