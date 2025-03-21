from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Supply, Uniform
from .serializers import SupplySerializer, UniformSerializer

class SupplyListView(APIView):
    def get(self, request):
        supplies = Supply.objects.all()
        serializer = SupplySerializer(supplies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplyDetailView(APIView):
    def get_object(self, pk):
        try:
            return Supply.objects.get(pk=pk)
        except Supply.DoesNotExist:
            return None

    def get(self, request, pk):
        supply = self.get_object(pk)
        if not supply:
            return Response({'error': 'Supply not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SupplySerializer(supply)
        return Response(serializer.data)

    def put(self, request, pk):
        supply = self.get_object(pk)
        if not supply:
            return Response({'error': 'Supply not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SupplySerializer(supply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        supply = self.get_object(pk)
        if not supply:
            return Response({'error': 'Supply not found'}, status=status.HTTP_404_NOT_FOUND)
        supply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UniformListView(APIView):
    def get(self, request):
        uniforms = Uniform.objects.all()
        serializer = UniformSerializer(uniforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UniformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UniformDetailView(APIView):
    def get_object(self, pk):
        try:
            return Uniform.objects.get(pk=pk)
        except Uniform.DoesNotExist:
            return None

    def get(self, request, pk):
        uniform = self.get_object(pk)
        if not uniform:
            return Response({'error': 'Uniform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UniformSerializer(uniform)
        return Response(serializer.data)

    def put(self, request, pk):
        uniform = self.get_object(pk)
        if not uniform:
            return Response({'error': 'Uniform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UniformSerializer(uniform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        uniform = self.get_object(pk)
        if not uniform:
            return Response({'error': 'Uniform not found'}, status=status.HTTP_404_NOT_FOUND)
        uniform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)