from django.db import models

class Menu_item(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False, unique=True)
    price = models.FloatField(null=True)
    spicy_level = models.PositiveSmallIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, default=None)
    cuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE, null=True, default=None)
    def __str__(self):
        return self.title
    def json(self):   
        return {
                "title": self.title,
                "description": self.description,
                "price": self.price,
                "spicy_level": self.spicy_level,
                "category": {
                    'title': self.category.title
                },
                "cuisine": {
                    'title': self.cuisine.title
                }
            }

class Category(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    def __str__(self):
        return self.title
# these are subclasses of the djangodb.models.Model