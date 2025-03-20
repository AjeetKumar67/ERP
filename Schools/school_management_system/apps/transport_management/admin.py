from django.contrib import admin
from .models import BusRoute, DriverAssignment

admin.site.register(BusRoute)
admin.site.register(DriverAssignment)