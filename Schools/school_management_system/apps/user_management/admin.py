# from django.contrib import admin
# from .models import User, UserProfile

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username', 'email', 'role', 'is_active']
#     list_filter = ['role', 'is_active']
#     search_fields = ['username', 'email']

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'address', 'date_of_birth']
#     search_fields = ['user__username', 'address']