from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')


def get_menu(request: HttpRequest, menu_name: str) -> HttpResponse:
    return render(request, 'main/index.html', context={'menu_name': menu_name})
