from django.shortcuts import render
from bdCars.models import Car
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    cars = Car.objects.all()
    return render(request, "bdCars/index.html", {
        "cars": cars
    })


def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    return render(request, "bdCars/car_detail.html", {
        "company": car.company,
        "country": car.country,
        "used": car.used
    })
