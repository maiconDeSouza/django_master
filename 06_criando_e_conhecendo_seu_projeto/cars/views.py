from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm


def home_cars_view(request):
    model = request.GET.get("search")
    if model:
        cars = Car.objects.filter(model__icontains=model).order_by('-pk')
        return render(request, 'cars/index.html', {"cars": cars})
    else:
        cars = Car.objects.all().order_by('-pk')
        return render(request, 'cars/index.html', {"cars": cars})


def new_car_view(request):
    if request.method == "POST":
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect("cars_list")
        else:
            # Se o formulário não for válido, renderiza a página novamente com os erros
            return render(request, 'cars/new_car.html', {'new_car_form': new_car_form})
    else:
        new_car_form = CarModelForm()
        return render(request, 'cars/new_car.html', {'new_car_form': new_car_form})
