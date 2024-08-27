from django.shortcuts import render


def home_cars(request):
    return render(request, 'cars/index.html', {"cars": {"model": "Astra"}})
