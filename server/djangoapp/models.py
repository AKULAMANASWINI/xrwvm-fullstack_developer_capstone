# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


# CarModel model
class CarModel(models.Model):
    # Car Type Choices
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES, default=SEDAN)
    year = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.year.year}) - {self.car_type}"
