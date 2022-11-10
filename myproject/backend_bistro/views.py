from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Menu_item, Categorie, Cuisine
from pprint import pprint


def get_menus(request):
    menus = list(Menu_item.objects.values()) # wrap in list(), because QuerySet is not JSON serializable
    pprint(menus)
    return JsonResponse({'data': menus})

#each view is responsible for returning HTTP response object, 
#containing the content for the requested page or raising exception
