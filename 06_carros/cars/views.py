from django.shortcuts import render


def cars_view(request):
    context = {
        "cars": {
            "model": "Astra 2.0"
        }
    }
    return render(request, 'cars.html', context)
