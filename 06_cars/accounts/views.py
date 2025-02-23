from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def registier_view(request):
    user_form = UserCreationForm(request.POST or None)
    context = {
        'user_form': user_form
    }

    if request.method == 'POST' and user_form.is_valid():
        user_form.save()
        return redirect('login')

    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('car_list')
    else:
        login_form = AuthenticationForm()

    context = {'login_form': login_form}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('car_list')
