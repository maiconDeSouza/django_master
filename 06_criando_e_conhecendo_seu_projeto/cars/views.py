from django.shortcuts import render
from cars.models import Car
from cars.forms import Carform


def home_cars_view(request):
    model = request.GET.get("search")
    if model:
        cars = Car.objects.filter(model__icontains=model).order_by('-pk')
        return render(request, 'cars/index.html', {"cars": cars})
    else:
        cars = Car.objects.all().order_by('-pk')
        return render(request, 'cars/index.html', {"cars": cars})


def new_car_view(request):
    new_car_form = Carform()
    return render(request, 'cars/new_car.html', {'new_car_form': new_car_form})
