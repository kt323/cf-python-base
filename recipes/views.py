from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
from .utils import get_chart
import pandas as pd

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
        recipe_name = request.POST.get('recipe_name')
        chart_type = request.POST.get('chart_type')

        qs = Recipes.objects.filter(name__icontains=recipe_name)

        if not qs.exists():
            context['recipes_df'] = "<p>Cannot match with your search criteria.</p>"
        else:
            recipes_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipes_df, labels=recipes_df['name'].values)

            context['recipes_df'] = recipes_df.to_html()
            context['chart'] = chart

    return render(request, 'recipes/recipes_search.html', context)



 