from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(request, "homepage/homepage.html")


