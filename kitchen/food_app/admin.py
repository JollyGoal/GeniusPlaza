from django.contrib import admin

from .models import Recipe, Ingredient, Step


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'pub_date', 'image')


class StepAdmin(admin.ModelAdmin):
    list_display = ('step_text', 'recipe', 'added')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Ingredient, IngredientAdmin)
