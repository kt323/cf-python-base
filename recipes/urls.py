from django.urls import path
from .views import home, RecipesListView, RecipesDetailView, search
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('list/', RecipesListView.as_view(), name='list'),
    path('detail/<int:pk>/', RecipesDetailView.as_view(), name='detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', search, name='search'),
]