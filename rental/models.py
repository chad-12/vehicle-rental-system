from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    price_per_day = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    days = models.IntegerField()

    def __str__(self):
        return f"{self.vehicle.name} - {self.days} days"