import django.core.exceptions
from django.shortcuts import render
from django.views import View

from django.views.generic import DetailView, ListView

from cookbook_app.models import Recipe
from django.http import JsonResponse

from unidecode import unidecode


class RecipeView(DetailView):
    template_name = "cookbook_app/recipe.html"
    model = Recipe
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["scaling_factors"] = {
            "1/4": 0.25,
            "1/2": 0.5,
            "2/3": 2 / 3,
            "3/4": 3 / 4,
            "1": 1,
            "1.5": 1.5,
            "2": 2,
        }
        return context


class RecipeListView(ListView):
    template_name = "cookbook_app/recipes.html"
    model = Recipe
    context_object_name = "recipes"
    ordering = ["name"]


class SearchRecipeView(View):
    def filter_unaccented(self, query, data):
        pass

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        try:
            search_results = Recipe.objects.filter(name__unaccent__icontains=query).order_by("name")
        except django.core.exceptions.FieldError:
            all_recipes = list(Recipe.objects.order_by("name"))
            search_results = filter(
                lambda recipe: unidecode(query).lower().strip() in unidecode(recipe.name).lower().strip(),
                all_recipes)

        context = {"recipes": search_results}
        return render(request, "cookbook_app/recipes_list.html", context)
