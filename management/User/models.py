from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('hr', 'HR'),
        ('finance', 'Finance'),
        ('sales', 'Sales'),
        ('inventory', 'Inventory'),
        ('purchase', 'Purchase'),
        ('production', 'Production'),
        ('marketing', 'Marketing'),
        ('crm', 'CRM'),
        ('support', 'Support'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')
    # role = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    signature = models.ImageField(upload_to='signatures/', blank=True, null=True)
    face_data = models.BinaryField(blank=True, null=True)
    fingerprint_data = models.BinaryField(blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)  # Add this line

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
