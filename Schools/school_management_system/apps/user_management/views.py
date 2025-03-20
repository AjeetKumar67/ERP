from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer
# from .serializers import UserSerializer
# from .serializers import UserProfileSerializer

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'user_management/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_management/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.phone = request.POST['phone']
        profile.address = request.POST['address']
        profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')
    return render(request, 'user_management/edit_profile.html', {'profile': profile})

def login_view(request):
    return HttpResponse("Login Page")

def register_view(request):
    return HttpResponse("Register Page")

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)
        return Response({
            "username": profile.user.username,
            "address": profile.address,
            "date_of_birth": profile.date_of_birth,
            "profile_picture": profile.profile_picture.url if profile.profile_picture else None,
        })