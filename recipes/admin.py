from django.contrib import admin
from .models import Recipes

# Register your models here.

admin.site.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_time')
    search_fields = ('name', 'ingredients')