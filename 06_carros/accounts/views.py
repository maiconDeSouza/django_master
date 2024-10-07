from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('car_list')
    else:
        # Exibe o formulário vazio para preenchimento
        user_creation_form = UserCreationForm()

    context = {
        'user_creation_form': user_creation_form
    }
    return render(request, 'register.html', context)
