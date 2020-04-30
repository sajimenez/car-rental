from django.contrib.auth import get_user_model
from django.db import models

from catalog.models import BaseModel, Car

User = get_user_model()


class Reservation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reservations')
    date_from = models.DateTimeField()
    date_until = models.DateTimeField()

    def __str__(self):
        return f'{self.id} - {self.user.username}'
