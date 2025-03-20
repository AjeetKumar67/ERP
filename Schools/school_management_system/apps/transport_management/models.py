from django.db import models

class BusRoute(models.Model):
    route_name = models.CharField(max_length=100)
    starting_point = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    stops = models.TextField()  # List of stops in a text format
    distance = models.FloatField()  # Distance in kilometers

    def __str__(self):
        return self.route_name


class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class DriverAssignment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    bus_route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.driver.name} - {self.bus_route.route_name}"


class TransportRequest(models.Model):
    student_name = models.CharField(max_length=100)
    bus_route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"{self.student_name} - {self.bus_route.route_name} ({self.status})"