from django.test import TestCase
from .models import BusRoute, DriverAssignment

class BusRouteModelTest(TestCase):
    def setUp(self):
        self.route = BusRoute.objects.create(
            route_name="Route A",
            start_location="Location A",
            end_location="Location B",
            distance=10.5
        )

    def test_bus_route_creation(self):
        self.assertEqual(self.route.route_name, "Route A")
        self.assertEqual(self.route.start_location, "Location A")
        self.assertEqual(self.route.end_location, "Location B")
        self.assertEqual(self.route.distance, 10.5)

class DriverAssignmentModelTest(TestCase):
    def setUp(self):
        self.assignment = DriverAssignment.objects.create(
            driver_name="John Doe",
            bus_route=self.route,
            assigned_date="2023-01-01"
        )

    def test_driver_assignment_creation(self):
        self.assertEqual(self.assignment.driver_name, "John Doe")
        self.assertEqual(self.assignment.bus_route, self.route)
        self.assertEqual(self.assignment.assigned_date, "2023-01-01")