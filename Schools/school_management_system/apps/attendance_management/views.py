from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance, Biometric
from .serializers import AttendanceSerializer, BiometricSerializer
from django.utils import timezone

class AttendanceView(APIView):
    def get(self, request):
        attendance_records = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        student_id = data.get('student_id')
        status_value = data.get('status')
        date = timezone.now().date()

        attendance_record, created = Attendance.objects.get_or_create(student_id=student_id, date=date)
        attendance_record.status = status_value
        attendance_record.save()

        serializer = AttendanceSerializer(attendance_record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AttendanceDetailView(APIView):
    def get(self, request, student_id):
        attendance_records = Attendance.objects.filter(student_id=student_id)
        serializer = AttendanceSerializer(attendance_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BiometricView(APIView):
    def get(self, request):
        biometric_records = Biometric.objects.all()
        serializer = BiometricSerializer(biometric_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = BiometricSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)