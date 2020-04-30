from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import ReservationForm
from .models import Reservation
from catalog.models import Car

User = get_user_model()


@csrf_exempt
@login_required
def book_car(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            user = request.user
            model_id = form.cleaned_data['model_id']
            date_from = form.cleaned_data['date_from']
            date_until = form.cleaned_data['date_until']
            cars = Car.objects.filter(model__id=model_id)
            cars = cars.exclude(reservations__date_until__gte=date_from)
            cars = cars.exclude(reservations__date_from__gte=date_until)
            if cars.exists():
                Reservation.objects.create(
                    user=user,
                    car=cars.first(),
                    date_from=date_from,
                    date_until=date_until
                )
                return JsonResponse({"msg": "Your reservation was successfull"})
    return JsonResponse({"msg": "There's no cars available for these dates"})
