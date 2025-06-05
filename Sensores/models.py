from django.db import models

# Create your models here.
class Sensor(models.Model):
    sensor_type = models.CharField()
    description = models.CharField()
    location = models.CharField()
    install_date = models.DateTimeField()

    def __str__(self):
        return self.type
