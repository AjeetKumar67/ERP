from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import SystemSetting
from .serializers import SystemSettingSerializer

class APIKeySettingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Placeholder for API key settings logic
        return Response({'message': 'API Key settings logic not implemented yet'}, status=status.HTTP_200_OK)

class SystemSettingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Placeholder for system settings logic
        return Response({'message': 'System settings logic not implemented yet'}, status=status.HTTP_200_OK)

class SettingsDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        settings = SystemSetting.objects.all()
        serializer = SystemSettingSerializer(settings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateSettingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, setting_id):
        try:
            setting = SystemSetting.objects.get(id=setting_id)
        except SystemSetting.DoesNotExist:
            return Response({'error': 'Setting not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SystemSettingSerializer(setting, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)