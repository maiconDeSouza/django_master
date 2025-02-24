from django.shortcuts import render, redirect
from .models import Car
from .forms import CarsForms
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin


# def cars_view(request):
#     cars = Car.objects.all()
#     search = request.GET.get('s')

#     if search:
#         cars = cars.filter(model__icontains=search)

#     context = {
#         'cars': cars
#     }
#     return render(request, 'index.html', context)


# class CarsView(View):
#     def get(self, request):
#         search = request.GET.get('s', '')

#         cars = Car.objects.filter(
#             model__icontains=search) if search else Car.objects.all()

#         context = {
#             'cars': cars
#         }
#         return render(request, 'index.html', context)


class CarsListView(ListView):
    model = Car
    template_name = 'index.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('s', '')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars

# def new_car(request):
#     new_car_form = CarsForms(request.POST or None, request.FILES or None)

#     if request.method == 'POST' and new_car_form.is_valid():
#         new_car_form.save()
#         return redirect('car_list')

#     return render(request, 'new_car.html', {'new_car_form': new_car_form})


# class NewCarView(View):

#     def post(self, request):
#         new_car_form = CarsForms(request.POST or None, request.FILES or None)

#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('car_list')

#         return render(request, 'new_car.html', {'new_car_form': new_car_form})

#     def get(self, request):
#         new_car_form = CarsForms()
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})


class NewCarCreateView(UserPassesTestMixin, CreateView):
    model = Car
    form_class = CarsForms
    template_name = 'new_car.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('/')
