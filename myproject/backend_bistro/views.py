from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Menu_item, Category, Cuisine
from pprint import pprint
import json


def get_menus(request):
    menus = list(Menu_item.objects.values()) # wrap in list(), because QuerySet is not JSON serializable
    pprint(menus)
    return JsonResponse({'data': menus})

def test(request):
    data = [i.json() for i in Menu_item.objects.all()]
    return HttpResponse(json.dumps(data), content_type = 'application/json')


# def get_menus_by_price(request, item_price):
#     menus = list(Menu_item.objects.filter(price=item_price).values())
#     pprint(menus)
#     return JsonResponse({'data': menus})

# def get_menu(request):
#     items = Menu_item.objects.all() #.all returns a queryset, .values a qs of dicts
#     data = []
#     for item in items:
#         cuisine = Cuisine.objects.get(id=item.cuisine_id)
#         category = Category.objects.get(id=item.category_id)
#         item_dict = {
#             "name": item.title,
#             "lower_case_name": item.title.lower(),
#             "cuisine": {
#                 Cuisine.objects.get(id=item.cuisine_id)
#                 # "id": cuisine.id,
#                 # "title": cuisine.title,
#             },
#             "category": category.title,
#         }
#         data.append(item_dict)
#     return JsonResponse(data, safe=False)

#each view is responsible for returning HTTP response object, 
#containing the content for the requested page or raising exception
