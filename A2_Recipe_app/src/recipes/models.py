from django.db import models

# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text="In minutes", default=0, null=True)
    ingredients = models.TextField(default='')
    description = models.TextField(default='')

    def __str__(self):
        return str(self.name)