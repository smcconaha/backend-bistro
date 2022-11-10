from django.db import models

class Menu_item(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    spicy_level = models.PositiveSmallIntegerField()
    category_id = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    cuisine_id = models.ForeignKey('Cuisine', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Categorie(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    def __str__(self):
        return self.title
# these are subclasses of the djangodb.models.Model