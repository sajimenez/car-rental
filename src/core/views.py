from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import CarModel, Reservation
from .serializer import ReservationSerializer


class CarModelListView(LoginRequiredMixin, ListView):
    model = CarModel
    paginate_by = 10


class CarModelDetailView(LoginRequiredMixin, DetailView):
    model = CarModel


class ReservationApiView(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated, )


class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
