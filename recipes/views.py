from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
from .utils import get_chart, rename_columns
import pandas as pd

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

def search(request):
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None
    chart = None
    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart
    }

    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name', '')
        chart_type = request.POST.get('chart_type', 'pie-chart')
        qs = Recipes.objects.filter(name__icontains=recipe_name)

        if qs.exists():
            recipes_df = pd.DataFrame(list(qs.values('id', 'name', 'cooking_time', 'ingredients', 'difficulty')))
            recipes_df = rename_columns(recipes_df)  
            chart = get_chart(chart_type, recipes_df)
            context['recipes_df'] = recipes_df.to_html(classes='table table-bordered', index=False)
            context['chart'] = chart
        else:
            context['recipes_df'] = "<p>Cannot match with your search criteria.</p>"
    return render(request, 'recipes/recipes_search.html', context)



 