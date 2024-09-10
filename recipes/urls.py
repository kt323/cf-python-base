from django.urls import path
from .views import home
from .views import RecipesListView, RecipesDetailView

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('list/', RecipesListView.as_view(), name='list'),
    path('detail/<int:pk>/', RecipesDetailView.as_view(), name='detail'),
]