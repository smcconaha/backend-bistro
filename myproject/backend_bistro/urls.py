from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_item_id>/', views.detail, name='detail'),
    path('<int:menu_item_id>/results/', views.results, name='results'),
]

# this is the URLconf