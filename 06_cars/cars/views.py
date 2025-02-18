from django.shortcuts import render
from .models import Car


def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('s')

    if search:
        cars = cars.filter(model__icontains=search)

    context = {
        'cars': cars
    }
    return render(request, 'index.html', context)
