from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Room, StudentHostel, HostelAttendance, HostelFee, RoomAllocation
from .serializers import (
    RoomSerializer,
    StudentHostelSerializer,
    HostelAttendanceSerializer,
    HostelFeeSerializer,
    RoomAllocationSerializer,
)

class RoomListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllocateRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        allocations = RoomAllocation.objects.all()
        serializer = RoomAllocationSerializer(allocations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomAllocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewAllocationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        allocations = RoomAllocation.objects.all()
        serializer = RoomAllocationSerializer(allocations, many=True)
        return Response(serializer.data)


class MarkAttendanceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = HostelAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewAttendanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attendance_records = HostelAttendance.objects.all()
        serializer = HostelAttendanceSerializer(attendance_records, many=True)
        return Response(serializer.data)