from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

class RecipesListView(ListView):
   model = Recipes
   template_name = 'recipes/recipes_list.html'
   context_object_name = 'recipes'

class RecipesDetailView(DetailView):
   model = Recipes
   template_name = 'recipes/recipes_detail.html'
   context_object_name = 'recipe'
