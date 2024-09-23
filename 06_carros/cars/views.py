from django.shortcuts import render
from django.http import HttpResponse


def cars_view(request):
    html = '''
    <html>
        <head>
            <title>Meus carros</title>
        </head>
        <body>
            <h1> Carros PycodeBR</h1>
            <h3>Só Carro Top!</h3>
        </body>
    </html>
'''
    return HttpResponse(html)
