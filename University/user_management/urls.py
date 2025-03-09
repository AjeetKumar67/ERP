from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet, PermissionViewSet, UserRoleViewSet, RolePermissionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'role-permissions', RolePermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('forgot-password/', UserViewSet.as_view({'post': 'forgot_password'}), name='forgot-password'),
    path('reset-password/', UserViewSet.as_view({'post': 'reset_password'}), name='reset-password'),
    path('logout/', UserViewSet.as_view({'post': 'logout'}), name='logout'),
]
