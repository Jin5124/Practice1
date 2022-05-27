from django.contrib import admin
from django.urls import path, include
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('youtube/', include('youtube.urls')),
]