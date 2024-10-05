from django.shortcuts import render
from .models import Car


def cars_view(request):
    cars = Car.objects.all()
    print(request.GET.get('search'))
    print(request.GET.get('name'))
    context = {
        "cars": cars
    }
    return render(request, 'cars.html', context)
