from django.db import models


class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField(default=0.0)  # New field to store humidity
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set when created

    def __str__(self):
        return f"Temp: {self.temperature}, Humidity: {self.humidity}, Time: {self.timestamp}"


