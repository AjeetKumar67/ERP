from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import BusRoute, DriverAssignment
from .serializers import BusRouteSerializer, DriverAssignmentSerializer


class BusRouteListView(APIView):
    def get(self, request):
        routes = BusRoute.objects.all()
        serializer = BusRouteSerializer(routes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BusRouteDetailView(APIView):
    def get(self, request, pk):
        route = get_object_or_404(BusRoute, pk=pk)
        serializer = BusRouteSerializer(route)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DriverAssignmentListView(APIView):
    def get(self, request):
        assignments = DriverAssignment.objects.all()
        serializer = DriverAssignmentSerializer(assignments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DriverAssignmentDetailView(APIView):
    def get(self, request, pk):
        assignment = get_object_or_404(DriverAssignment, pk=pk)
        serializer = DriverAssignmentSerializer(assignment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBusRouteView(APIView):
    def post(self, request):
        serializer = BusRouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDriverAssignmentView(APIView):
    def post(self, request):
        serializer = DriverAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateBusRouteView(APIView):
    def put(self, request, pk):
        route = get_object_or_404(BusRoute, pk=pk)
        serializer = BusRouteSerializer(route, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDriverAssignmentView(APIView):
    def put(self, request, pk):
        assignment = get_object_or_404(DriverAssignment, pk=pk)
        serializer = DriverAssignmentSerializer(assignment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteBusRouteView(APIView):
    def delete(self, request, pk):
        route = get_object_or_404(BusRoute, pk=pk)
        route.delete()
        return Response({'message': 'Bus route deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class DeleteDriverAssignmentView(APIView):
    def delete(self, request, pk):
        assignment = get_object_or_404(DriverAssignment, pk=pk)
        assignment.delete()
        return Response({'message': 'Driver assignment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)