from django.shortcuts import render

from django.views.generic import DetailView

from cookbook_app.models import Recipe


class RecipeView(DetailView):
    template_name = "cookbook_app/recipe.html"
    model = Recipe
