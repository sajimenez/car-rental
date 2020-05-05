from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework import serializers

from . import models


class ReservationSerializer(serializers.ModelSerializer):
    model_id = serializers.IntegerField(source='car.car_model.id',)

    class Meta:
        model = models.Reservation
        fields = ('model_id', 'date_from', 'date_until',)
        extra_kwargs = {
            'date_from': {'input_formats': ('%d/%m/%Y %H:%M', )},
            'date_until': {'input_formats': ('%d/%m/%Y %H:%M', )},
        }

    def validate_date_from(self, date_from):
        if date_from < timezone.now():
            raise serializers.ValidationError(_("Date from must be grater than current datetime"))
        return date_from

    def validate(self, data):
        date_from = data['date_from']
        date_until = data['date_until']

        if date_from >= date_until:
            raise serializers.ValidationError(_("Date until must be greater than date from"))

        user = self.context['request'].user
        users_active_reservations = self.Meta.model.objects.filter(user=user, is_active=True)
        if users_active_reservations.count() >= 5:
            raise serializers.ValidationError(_("Users can't have more that 5 active reservations"))

        # Remove model_id from data
        car = data.pop('car')
        model_id = car['car_model']['id']

        # Find available cars
        cars = models.Car.objects.filter(car_model__id=model_id)
        cars = cars.exclude(reservations__is_active=False)
        cars = cars.exclude(
            reservations__date_until__gte=date_from - timezone.timedelta(hours=2),
            # Cars are available after 2 hours of been returned
            reservations__date_from__lte=date_until + timezone.timedelta(hours=2)
        )

        if cars.exists():
            data.update({'car': cars.first(), 'user': user})
            return data
        raise serializers.ValidationError(_("There's no car available for the given date"))
