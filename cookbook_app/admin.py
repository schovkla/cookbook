from django.contrib import admin
from django.template.loader import get_template

import cookbook_app.models
from cookbook_app.models import Tag, Ingredient, Recipe, Unit, Step


# TODO: Migrate admin to Baton

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


class StepInline(admin.TabularInline):
    model = Step


class IngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    fields = ("ingredient", "value", "unit")


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ("name", "tags", "note")
    filter_horizontal = ("tags",)
    inlines = (StepInline, IngredientInline)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass
