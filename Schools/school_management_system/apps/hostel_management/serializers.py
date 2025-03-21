from rest_framework import serializers
from .models import Room, StudentHostel, HostelAttendance, HostelFee, RoomAllocation

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'capacity', 'amenities']


class StudentHostelSerializer(serializers.ModelSerializer):
    student_username = serializers.ReadOnlyField(source='student.username')
    room_number = serializers.ReadOnlyField(source='room.room_number')

    class Meta:
        model = StudentHostel
        fields = ['id', 'student', 'student_username', 'room', 'room_number', 'check_in_date', 'check_out_date']


class HostelAttendanceSerializer(serializers.ModelSerializer):
    student_username = serializers.ReadOnlyField(source='student_hostel.student.username')

    class Meta:
        model = HostelAttendance
        fields = ['id', 'student_hostel', 'student_username', 'date', 'status']


class HostelFeeSerializer(serializers.ModelSerializer):
    student_username = serializers.ReadOnlyField(source='student_hostel.student.username')

    class Meta:
        model = HostelFee
        fields = ['id', 'student_hostel', 'student_username', 'amount_due', 'amount_paid', 'due_date']


class RoomAllocationSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = RoomAllocation
        fields = ['id', 'student', 'student_name', 'room_number', 'allocation_date', 'deallocation_date']