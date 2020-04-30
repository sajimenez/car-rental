from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def deactivate(self):
        self.is_active = False
        self.save()


class CarModel(BaseModel):
    class CarDoors(models.IntegerChoices):
        TWO = 2
        FOUR = 4
        FIVE = 5

    class CarSize(models.TextChoices):
        MINICOMPACT = 'minicompact'
        COMPACT = 'compact'
        VAN = 'van'
        PICKUP = 'pickup'

    name = models.CharField(max_length=255)
    doors = models.IntegerField(choices=CarDoors.choices)
    is_diesel = models.BooleanField(default=False)
    size = models.CharField(max_length=50, choices=CarSize.choices)

    def __str__(self):
        return self.name


class Car(BaseModel):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f'{self.id} - {self.model.name}'
