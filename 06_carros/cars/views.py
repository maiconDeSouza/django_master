from typing import Any
# from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Car
from .form import CarModelForm
from django.urls import reverse_lazy
# from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


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

# class CarsView(View):
#     def get(self, request):
#         cars = {}
#         search = request.GET.get('search')

#         if search:
#             cars = Car.objects.filter(
#                 model__icontains=search).order_by('model')
#         else:
#             cars = Car.objects.all().order_by('model')

#         context = {
#             "cars": cars
#         }
#         return render(request, 'cars.html', context)

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            return super().get_queryset().filter(model__icontains=search).order_by('model')
        else:
            return super().get_queryset().order_by('model')


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


# class NewCarView(View):
#     def get(self, request):
#         new_car_from = CarModelForm()
#         context = {
#             "new_car_form": new_car_from
#         }
#         return render(request, 'new_car.html', context)

#     def post(self, request):
#         new_car_from = CarModelForm(request.POST, request.FILES)
#         if new_car_from.is_valid():
#             new_car_from.save()
#             return redirect('cars_list')
#         else:
#             new_car_form = CarModelForm()
#             context = {
#                 "new_car_form": new_car_form
#             }
#             return render(request, 'new_car.html', context)

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdatelView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    form_class = CarModelForm

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
