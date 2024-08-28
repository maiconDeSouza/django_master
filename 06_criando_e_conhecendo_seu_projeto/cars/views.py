from django.shortcuts import render
from cars.models import Car


def home_cars(request):
    model = request.GET.get("search")
    if model:
        cars = Car.objects.filter(model__icontains=model).order_by('-pk')
        return render(request, 'cars/index.html', {"cars": cars})
    else:
        cars = Car.objects.all().order_by('-pk')
        return render(request, 'cars/index.html', {"cars": cars})
