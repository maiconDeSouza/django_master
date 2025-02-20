from django.shortcuts import render
from .models import Car
from .forms import CarsForms


def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('s')

    if search:
        cars = cars.filter(model__icontains=search)

    context = {
        'cars': cars
    }
    return render(request, 'index.html', context)


def new_car(request):
    new_car_form = CarsForms()
    context = {
        'new_car_form': new_car_form
    }
    return render(request, 'new_car.html', context)
