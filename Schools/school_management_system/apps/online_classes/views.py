from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClassSession, Assignment
from .serializers import ClassSessionSerializer, AssignmentSerializer

class ClassSessionListView(APIView):
    def get(self, request):
        sessions = ClassSession.objects.all()
        serializer = ClassSessionSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ClassSessionDetailView(APIView):
    def get(self, request, pk):
        try:
            session = ClassSession.objects.get(pk=pk)
            serializer = ClassSessionSerializer(session)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ClassSession.DoesNotExist:
            return Response({'error': 'Class session not found'}, status=status.HTTP_404_NOT_FOUND)

class AssignmentListView(APIView):
    def get(self, request):
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AssignmentDetailView(APIView):
    def get(self, request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
            serializer = AssignmentSerializer(assignment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Assignment.DoesNotExist:
            return Response({'error': 'Assignment not found'}, status=status.HTTP_404_NOT_FOUND)

class CreateClassSessionView(APIView):
    def post(self, request):
        serializer = ClassSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateAssignmentView(APIView):
    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JoinClassSessionView(APIView):
    def post(self, request, pk):
        try:
            session = ClassSession.objects.get(pk=pk)
            # Logic for a student to join a class session
            # Example: session.students.add(request.user)
            return Response({'message': 'Joined class session successfully'}, status=status.HTTP_200_OK)
        except ClassSession.DoesNotExist:
            return Response({'error': 'Class session not found'}, status=status.HTTP_404_NOT_FOUND)

class SubmitAssignmentView(APIView):
    def post(self, request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
            # Logic for a student to submit an assignment
            # Example: assignment.submitted_by.add(request.user)
            return Response({'message': 'Assignment submitted successfully'}, status=status.HTTP_200_OK)
        except Assignment.DoesNotExist:
            return Response({'error': 'Assignment not found'}, status=status.HTTP_404_NOT_FOUND)