from django.urls import path

from .views import CarModelListView

urlpatterns = [
    path('', CarModelListView.as_view(), name='carmodel-list'),
]
