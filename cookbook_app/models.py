from django.db import models
from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Tag(models.Model):
    name = models.CharField(max_length=127, verbose_name=_("Name"), unique=True)
    color = ColorField(default="#0000FF", verbose_name=_("Color"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=127, verbose_name=_("Name"), unique=True)

    class Meta:
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")

    def __str__(self):
        return self.name


class Step(models.Model):
    description = models.TextField(verbose_name=_("Description"))
    order = models.IntegerField(verbose_name=_("Order"))
    recipe = models.ForeignKey("cookbook_app.Recipe", on_delete=models.CASCADE, related_name="steps",
                               verbose_name=_("Recipe"))

    class Meta:
        verbose_name = _("Step")
        verbose_name_plural = _("Steps")
        unique_together = ("order", "recipe")

    def __str__(self):
        return self.description


class Unit(models.Model):
    name = models.CharField(max_length=63, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")

    def __str__(self):
        return self.name


class Amount(models.Model):
    value = models.FloatField(default=0, verbose_name=_("Value"))
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="+", verbose_name=_("Unit"))
    recipe = models.ForeignKey("cookbook_app.Recipe", on_delete=models.CASCADE, related_name="amount",
                               verbose_name=_("Recipe"))
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="amount",
                                   verbose_name=_("Ingredient"))

    class Meta:
        verbose_name = _("Amount")
        verbose_name_plural = _("Amounts")


class Recipe(TimeStampedModel):
    name = models.CharField(max_length=127, verbose_name=_("Name"), unique=True)
    note = models.TextField(null=True, blank=True, verbose_name=_("Note"))
    tags = models.ManyToManyField(Tag, related_name='recipes', blank=True, verbose_name=_("Tags"))
    ingredients = models.ManyToManyField(Ingredient, through=Amount, related_name='recipes', blank=True,
                                         verbose_name=_("Ingredients"))

    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

    def __str__(self):
        return self.name
