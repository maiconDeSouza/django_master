from django.shortcuts import render

context = {
    'cars': {
        'model': 'Astra 2.0'
    }
}


def cars_view(request):
    return render(request, 'index.html', context)
