from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint


def index(request):
    return HttpResponse("Hello, world. You're at the bistro index.")

def detail(request, menu_item_id):
    return HttpResponse("You're looking at menu item %s." % menu_item_id)

def results(request, menu_item_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % menu_item_id)

#each view is responsible for returning HTTP response object, containing the contect for the requested page or raising exception
