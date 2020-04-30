from django.urls import path

from .views import book_car

urlpatterns = [
    path('book/', book_car, name='book-car'),
]
