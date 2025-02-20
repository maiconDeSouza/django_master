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
    if request.method == 'POST':
        new_car_form = CarsForms(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('car_list')
    else:
        new_car_form = CarsForms()
        context = {
            'new_car_form': new_car_form
        }
        return render(request, 'new_car.html', context)
