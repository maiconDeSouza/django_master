from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Car
from .forms import CarsForms

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
        return redirect('/login/')


class CarDetail(DetailView):
    model = Car
    template_name = 'detail_car.html'
    context_object_name = 'car'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdate(UpdateView):
    model = Car
    form_class = CarsForms
    template_name = 'update_car.html'

    def get_success_url(self):
        context = {
            'pk': self.object.pk
        }
        return reverse_lazy('car_detail', kwargs=context)


class CarDelete(UserPassesTestMixin, DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('/login/')
