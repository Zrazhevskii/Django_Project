from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    measuring_temp = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_measurement = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

