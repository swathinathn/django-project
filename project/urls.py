from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from myapp import views

urlpatterns = [
    path('', lambda request: redirect('home')),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
]