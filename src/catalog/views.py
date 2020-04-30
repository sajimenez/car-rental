from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from .models import CarModel


class CarModelListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = CarModel
    paginate_by = 50
