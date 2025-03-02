from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'password', 'role', 'mobile_number', 'address', 
            'profile', 'profile_picture', 'signature', 'face_data', 'fingerprint_data'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role'],
            mobile_number=validated_data.get('mobile_number', ''),
            address=validated_data.get('address', ''),
            profile=validated_data.get('profile', ''),
            profile_picture=validated_data.get('profile_picture', None),
            signature=validated_data.get('signature', None),
            face_data=validated_data.get('face_data', None),
            fingerprint_data=validated_data.get('fingerprint_data', None),
            is_active=False  # Set user as inactive initially
        )
        self.send_otp(user)
        return user

    def send_otp(self, user):
        otp = get_random_string(length=6, allowed_chars='0123456789')
        user.otp = otp
        user.save()
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp}',
            'from@example.com',  # Replace with your actual sender email
            [user.email],
            fail_silently=False,
        )

class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'], otp=data['otp'])
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid OTP or email')
        user.is_active = True
        user.otp = ''
        user.save()
        return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid login credentials")
            if not user.is_active:
                raise serializers.ValidationError("User account is not active")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")

        data['user'] = user
        return data

class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('mobile_number', 'address', 'profile', 'profile_picture', 'signature', 'face_data', 'fingerprint_data')

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist")
        return value

    def save(self):
        user = User.objects.get(email=self.validated_data['email'])
        otp = get_random_string(length=6, allowed_chars='0123456789')
        user.otp = otp
        user.save()
        send_mail(
            'Password Reset OTP',
            f'Your OTP for password reset is {otp}',
            'from@example.com',  # Replace with your actual sender email
            [user.email],
            fail_silently=False,
        )

class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'], otp=data['otp'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or email")
        return data

    def save(self):
        user = User.objects.get(email=self.validated_data['email'])
        user.set_password(self.validated_data['new_password'])
        user.otp = ''
        user.save()