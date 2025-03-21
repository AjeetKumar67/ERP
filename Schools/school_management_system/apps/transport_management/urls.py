from django.urls import path
from .views import (
    BusRouteListView,
    BusRouteDetailView,
    DriverAssignmentListView,
    DriverAssignmentDetailView,
    CreateBusRouteView,
    CreateDriverAssignmentView,
    UpdateBusRouteView,
    UpdateDriverAssignmentView,
    DeleteBusRouteView,
    DeleteDriverAssignmentView,
)

urlpatterns = [
    path('routes/', BusRouteListView.as_view(), name='bus-route-list'),
    path('routes/<int:pk>/', BusRouteDetailView.as_view(), name='bus-route-detail'),
    path('routes/create/', CreateBusRouteView.as_view(), name='create-bus-route'),
    path('routes/update/<int:pk>/', UpdateBusRouteView.as_view(), name='update-bus-route'),
    path('routes/delete/<int:pk>/', DeleteBusRouteView.as_view(), name='delete-bus-route'),

    path('assignments/', DriverAssignmentListView.as_view(), name='driver-assignment-list'),
    path('assignments/<int:pk>/', DriverAssignmentDetailView.as_view(), name='driver-assignment-detail'),
    path('assignments/create/', CreateDriverAssignmentView.as_view(), name='create-driver-assignment'),
    path('assignments/update/<int:pk>/', UpdateDriverAssignmentView.as_view(), name='update-driver-assignment'),
    path('assignments/delete/<int:pk>/', DeleteDriverAssignmentView.as_view(), name='delete-driver-assignment'),
]