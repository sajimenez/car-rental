from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import CarModel
from reservation.forms import ReservationForm


class CarModelListView(LoginRequiredMixin, ListView):
    model = CarModel
    paginate_by = 50


class CarModelDetailView(LoginRequiredMixin, DetailView):
    model = CarModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReservationForm()
        return context
