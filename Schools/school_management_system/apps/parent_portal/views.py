from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import ChildProgress, PaymentAlert
from .serializers import ChildProgressSerializer, PaymentAlertSerializer

class ChildProgressAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        progress_records = ChildProgress.objects.filter(user=request.user)
        serializer = ChildProgressSerializer(progress_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ChildProgressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentAlertAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        alerts = PaymentAlert.objects.filter(user=request.user, is_active=True)
        serializer = PaymentAlertSerializer(alerts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PaymentAlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)