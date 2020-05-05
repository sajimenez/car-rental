from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this object should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    def deactivate(self):
        self.is_active = False
        self.save()


class UserManager(BaseUserManager):
    def create_user(self, username, password):
        user = self.model(username=username, password=password)
        self.model.save()
        return user


class User(BaseModel, AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def check_password(self, raw_password):
        return self.password == raw_password


class CarModel(BaseModel):
    class Meta:
        verbose_name = _('car model')
        verbose_name_plural = _('car models')

    class CarDoors(models.IntegerChoices):
        TWO = 2
        FOUR = 4
        FIVE = 5

    class CarSize(models.TextChoices):
        MINICOMPACT = 'minicompact', _('Minicompact')
        COMPACT = 'compact', _('Compact')
        VAN = 'van', _('Van')
        PICKUP = 'pickup', _('Pick up')

    name = models.CharField(_('name'), max_length=255)
    doors = models.IntegerField(_('doors'), choices=CarDoors.choices)
    is_diesel = models.BooleanField(_('is diesel'), default=False)
    size = models.CharField(_('size'), max_length=64, choices=CarSize.choices)

    def __str__(self):
        return self.name


class Car(BaseModel):
    class Meta:
        verbose_name = _('car')
        verbose_name_plural = _('cars')

    car_model = models.ForeignKey(
        CarModel,
        verbose_name=_('car model'),
        on_delete=models.CASCADE,
        related_name='cars'
    )

    def __str__(self):
        return f'{self.id} - {self.car_model.name}'


class Reservation(BaseModel):
    class Meta:
        verbose_name = _('reservation')
        verbose_name_plural = _('reservations')

    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    car = models.ForeignKey(
        Car,
        verbose_name=_('car'),
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    date_from = models.DateTimeField(_('date from'))
    date_until = models.DateTimeField(_('date until'))

    def __str__(self):
        return f'{self.id} - {self.user.username}'
