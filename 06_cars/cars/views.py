from django.shortcuts import render, redirect
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
    new_car_form = CarsForms(request.POST or None, request.FILES or None)

    if request.method == 'POST' and new_car_form.is_valid():
        new_car_form.save()
        return redirect('car_list')

    return render(request, 'new_car.html', {'new_car_form': new_car_form})
