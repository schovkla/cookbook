import django.core.exceptions
from django.shortcuts import render
from django.views import View

from django.views.generic import DetailView, ListView

from cookbook_app.models import Recipe, Tag
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["all_tags"] = Tag.objects.all()
        return context


class SearchRecipeView(View):
    def post(self, request, *args, **kwargs):
        query = request.POST.get("query", "")
        try:
            search_results = Recipe.objects.filter(name__unaccent__icontains=query).order_by("name")
        except django.core.exceptions.FieldError:
            all_recipes = list(Recipe.objects.order_by("name"))
            search_results = filter(
                lambda recipe: unidecode(query).lower().strip() in unidecode(recipe.name).lower().strip(),
                all_recipes)

        context = {"recipes": search_results}
        return render(request, "cookbook_app/recipes_list.html", context)


class UpdateNoteView(View):
    def post(self, request, *args, **kwargs):
        recipe_id = request.POST.get("recipe_id", None)
        new_note = request.POST.get("new_note", "")

        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            recipe.note = new_note
            recipe.save()
            return JsonResponse({"success": True})
        except Recipe.DoesNotExist:
            return JsonResponse({"success": False, "error": "Recipe does not exists"})
