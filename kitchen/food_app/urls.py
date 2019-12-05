from django.urls import path
from .views import *

urlpatterns = [
    path('steps/', StepView.as_view()),
    path('register/', CreateUserView.as_view()),
    path('users/', UserList.as_view()),
    path('ingredients/', IngredientsView.as_view()),
    path('recipes_list/', RecipesList.as_view()),
    path('recipes/', RecipesView.as_view()),
]
