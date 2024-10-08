from django.shortcuts import render, redirect
from .models import Car
from .form import CarModelForm
from django.views import View


# def cars_view(request):
#     cars = {}
#     search = request.GET.get('search')

#     if search:
#         cars = Car.objects.filter(model__icontains=search).order_by('model')
#     else:
#         cars = Car.objects.all().order_by('model')

#     context = {
#         "cars": cars
#     }
#     return render(request, 'cars.html', context)

class CarsView(View):
    def get(self, request):
        cars = {}
        search = request.GET.get('search')

        if search:
            cars = Car.objects.filter(
                model__icontains=search).order_by('model')
        else:
            cars = Car.objects.all().order_by('model')

        context = {
            "cars": cars
        }
        return render(request, 'cars.html', context)


# def new_car_view(requets):
#     new_car_form = CarModelForm()
#     if requets.method == 'POST':
#         new_car_form = CarModelForm(requets.POST, requets.FILES)

#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')

#     context = {
#         "new_car_form": new_car_form
#     }

#     return render(requets, 'new_car.html', context)


class NewCarView(View):
    def get(self, request):
        new_car_from = CarModelForm()
        context = {
            "new_car_form": new_car_from
        }
        return render(request, 'new_car.html', context)

    def post(self, request):
        new_car_from = CarModelForm(request.POST, request.FILES)
        if new_car_from.is_valid():
            new_car_from.save()
            return redirect('cars_list')
        else:
            new_car_form = CarModelForm()
            context = {
                "new_car_form": new_car_form
            }
            return render(request, 'new_car.html', context)
