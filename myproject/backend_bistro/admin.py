from django.contrib import admin

from .models import Menu_item, Category, Cuisine

admin.site.register(Menu_item)
admin.site.register(Category)
admin.site.register(Cuisine)
