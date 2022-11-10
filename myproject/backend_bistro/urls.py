from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.get_menus),
    # path('menu/<str:title>/', views.get_menu),
]

# this is the URLconf