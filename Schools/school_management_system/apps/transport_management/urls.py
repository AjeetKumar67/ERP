from django.urls import path
from .views import BusRouteListView, AssignDriverView, GPSIntegrationView

urlpatterns = [
    path('routes/', BusRouteListView.as_view(), name='bus-route-list'),
    path('assign-driver/', AssignDriverView.as_view(), name='assign-driver'),
    path('gps/', GPSIntegrationView.as_view(), name='gps-integration'),
]