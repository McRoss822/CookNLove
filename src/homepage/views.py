from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(request, "homepage.html")


def about_us(request):
    return render(request, "homepage/about_us.html")
