from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField(blank=True)

    def __str__(self):
        return f"Room {self.room_number} (Capacity: {self.capacity})"


class StudentHostel(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.username} - Room {self.room.room_number}"


class HostelAttendance(models.Model):
    student_hostel = models.ForeignKey(StudentHostel, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=True)  # True for present, False for absent

    def __str__(self):
        return f"Attendance for {self.student_hostel.student.username} on {self.date}"


class HostelFee(models.Model):
    student_hostel = models.ForeignKey(StudentHostel, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateField()

    def __str__(self):
        return f"Fee for {self.student_hostel.student.username} - Due: {self.amount_due}"


class RoomAllocation(models.Model):
    student = models.ForeignKey('student_management.Student', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    allocation_date = models.DateField()
    deallocation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.student}"