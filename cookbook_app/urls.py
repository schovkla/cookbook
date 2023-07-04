from django.urls import path

from cookbook_app.views import RecipeView, RecipeListView, SearchRecipeView

urlpatterns = [
    path("recipe/<int:pk>/", RecipeView.as_view(), name="recipe"),
    path("recipes/", RecipeListView.as_view(), name="recipes"),
    path("search_recipes/", SearchRecipeView.as_view(), name='search_recipes'),
]
