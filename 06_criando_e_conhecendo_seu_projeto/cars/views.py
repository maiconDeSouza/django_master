from django.shortcuts import render
from django.http import HttpResponse


def home_cars(request):
    return HttpResponse('Bem Vindo a nossa agencia de carros')
