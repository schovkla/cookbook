from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from cookbook_app.views import RecipeView, RecipeListView, SearchRecipeView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('recipes'), permanent=True)),
    path("recipe/<int:pk>/", RecipeView.as_view(), name="recipe"),
    path("recipes/", RecipeListView.as_view(), name="recipes"),
    path("search_recipes/", SearchRecipeView.as_view(), name='search_recipes'),
]
