from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.testing),
    path('menu/', views.menu),
]

# this is the URLconf