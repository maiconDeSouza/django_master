from django.shortcuts import render
from .models import Car


def cars_view(request):
    search = request.GET.get('s')
    print(search)
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'index.html', context)
