
from django.contrib import admin
from django.urls import path, include
from myopenai.views import generate_response
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]
