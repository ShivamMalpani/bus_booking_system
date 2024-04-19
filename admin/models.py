from django.db import models

class Bus(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    cities = models.CharField(max_length=200)  # Storing cities as a comma-separated string
    info = models.TextField()
    seat_status = models.TextField()
    available_days = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class BusBookingHistory(models.Model):
    bus = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return self.bus + ' - ' + self.user



