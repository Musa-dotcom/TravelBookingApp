from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_date = models.DateField()

class Hotel(models.Model):
    check_in_time = models.DateTimeField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

class Flight(models.Model):
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

class CarRental(models.Model):
    car_model = models.CharField(max_length=255)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

class Destination(models.Model):
    routes = models.CharField(max_length=255)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

class Activity(models.Model):
    activity_list = models.CharField(max_length=255)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

class PaymentDetails(models.Model):
    payment_info = models.CharField(max_length=255)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)


# Create your models here.
