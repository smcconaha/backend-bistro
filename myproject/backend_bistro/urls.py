from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.get_menus),
    path('menu/test/', views.test),
]

# this is the URLconf