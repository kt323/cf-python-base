from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

class RecipesListView(LoginRequiredMixin, ListView):
   model = Recipes
   template_name = 'recipes/recipes_list.html'
   context_object_name = 'recipes'

class RecipesDetailView(LoginRequiredMixin, DetailView):
   model = Recipes
   template_name = 'recipes/recipes_detail.html'
   context_object_name = 'recipe'


 