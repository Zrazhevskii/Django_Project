from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=80, verbose_name='Датчик')
    description = models.CharField(max_length=250, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Датчик', related_name='measurements', blank=True)
    measuring_temp = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Измерение')
    time_of_measurement = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-time_of_measurement']
