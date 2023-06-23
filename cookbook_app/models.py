from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField


class Recipe(models.Model):
    name = models.CharField(max_length=127);
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    tags = models.ManyToManyField('Tag', related_name='recipes', blank=True)
    ingredients = models.ManyToManyField('Ingredient', through='Amount', related_name='recipes', blank=True)

    def save(self, *args, **kwargs):
        """ On save, update timestamps"""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, *kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=127)
    color = ColorField(defaul='#0000FF')

    def __str__(self):
        return self.name


class Step(models.Model):
    description: models.TextField()
    order: int

    def __str__(self):
        return self.description


class Ingredient(models.Model):
    name: models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Amount(models.Model):
    value: float
    recipe: models.ForeignKey(Recipe, on_delete=models.SET_NULL)
    ingredient: models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit: models.CharField(max_length=63)
