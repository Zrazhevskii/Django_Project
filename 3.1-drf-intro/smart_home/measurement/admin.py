from django.contrib import admin

# Register your models here.
from measurement.models import Sensor, Measurement


admin.site.register(Sensor)

admin.site.register(Measurement)

