from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.car_detail, name="car-detail")
]
