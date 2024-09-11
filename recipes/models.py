from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text="In minutes", default=0, null=True)
    ingredients = models.TextField(default='')
    description = models.TextField(default='')
    pic = models.ImageField(upload_to='recipe_pics', default='no_picture.jpg')
    difficulty = models.CharField(max_length=20, blank=True, null=True)

    def return_ingredients_as_list(self):
        return self.ingredients.all('')

    def get_absolute_url(self):
        return reverse('recipes_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)