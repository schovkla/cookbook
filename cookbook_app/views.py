from django.shortcuts import render

from django.views.generic import DetailView, ListView

from cookbook_app.models import Recipe
from django.http import JsonResponse
from django.views.decorators.http import require_GET


class RecipeView(DetailView):
    template_name = "cookbook_app/recipe.html"
    model = Recipe
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["scalingFactors"] = {
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


@require_GET
def search_recipes(request):
    query = request.GET.get('query', '')
    # TODO: make it czech accents insensitive
    search_results = Recipe.objects.filter(name__icontains=query)
    results_data = [{'pk': recipe.pk, 'name': recipe.name} for recipe in search_results]
    return JsonResponse(results_data, safe=False)
