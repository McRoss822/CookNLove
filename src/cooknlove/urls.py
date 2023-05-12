
from django.contrib import admin
from django.urls import path, include
from myopenai.views import generate_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('reg/', include('myopenai.urls'))
]
