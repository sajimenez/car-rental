from django.urls import path

from .views import CarModelListView, CarModelDetailView

urlpatterns = [
    path('', CarModelListView.as_view(), name='carmodel-list'),
    path('<int:pk>', CarModelDetailView.as_view(), name='carmodel-detail'),
]
