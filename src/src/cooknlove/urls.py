
from django.contrib import admin
from django.urls import path, include
from myopenai.views import generate_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('', generate_response , name='generate_response'),
    path('reg/', include('myopenai.urls'))
]
