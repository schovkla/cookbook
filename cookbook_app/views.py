from django.shortcuts import render

from django.views.generic import DetailView

from cookbook_app.models import Recipe


class RecipeView(DetailView):
    template_name = "cookbook_app/recipe.html"
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['steps'] = recipe.steps.all()
        return context

