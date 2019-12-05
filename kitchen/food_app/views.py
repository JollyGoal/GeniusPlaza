from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView

from .serializers import *


# class OneMoreWayToAddData(CreateAPIView):
#     """
#     POST:
#     Creator class
#     ###Fileds should be sent:
#         {
#             'step_text': Some Text,
#             'recipe': 1,
#             'added': DateTime
#         }
#     + added - ***Optional***
#     """
#     permission_classes = [permissions.AllowAny]
#     queryset = Step.objects.all()
#     serializer_class = StepSerializer


class StepView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    """
    DELETE:
    Delete step
    ###Params should be sent:
        {
            'id': 1,
        }
    """
    def delete(self, request):
        step_id = request.GET.get('id')
        step = Step.objects.filter(id=step_id)
        step.delete()
        return Response({'status': 'Deleted'})

    """
    GET:
    Get all the steps by recipe id
    ###Params should be sent:
        {
            'recipe_id': 1,
        }
    """
    def get(self, request):
        recipe_id = request.GET.get('recipe_id')
        steps = Step.objects.filter(recipe=recipe_id).order_by('-added')
        serializer = StepSerializer(steps, many=True)
        return Response({'data': serializer.data})

    """
    POST:
    Creator class
    ###Fileds should be sent:
        {
            'step_text': Some Text,
            'recipe': 1,
            'added': DateTime
        }
    + added - ***Optional***
    """
    def post(self, request):
        step = StepSerializer(data=request.data)
        if step.is_valid():
            step.save()
            return Response({'status': 'Added'})
        else:
            return Response({'status': 'Error'})


class UserList(APIView):

    """
    GET:
    Get all the users
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'data': serializer.data})


class CreateUserView(CreateAPIView, APIView):
    """
    POST:
    Creator class
    ###Fileds should be sent:
        {
            'username': User,
            'password': some_password,
            'email': example@mail.com,
            'first_name': Alan,
            'last_name': Alanov,
        }
    """
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class IngredientsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    """
    DELETE:
    Delete an ingredient
    ###Params should be sent:
        {
            'ingredients_id': 1,
        }
    """
    def delete(self, request):
        ingredients_id = request.GET.get('id')
        ingredients = Step.objects.filter(id=ingredients_id)
        ingredients.delete()
        return Response({'status': 'Deleted'})

    """
    GET:
    Get all the ingredients
    """
    def get(self, request):
        ingredient = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredient, many=True)
        return Response({'data': serializer.data})

    """
    POST:
    Creator class
    ###Fileds should be sent:
        {
            'name': Sugar,
            'price': 123,
        }
    """
    def post(self, request):
        ingredient = IngredientSerializer(data=request.data)
        if ingredient.is_valid():
            ingredient.save()
            return Response({'status': 'Added'})
        else:
            return Response({'status': 'Error'})


class RecipesList(ListAPIView):
    """
    GET:
    Get all the recipes list with pagination
        Page size: 6
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = PageNumberPagination


class RecipesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    """
    GET:
    Get all recipes by particular user
    ###Params should be sent:
        {
            'user': 1,
        }
    """
    def get(self, request):
        user = request.GET.get('user')
        recipes = Recipe.objects.filter(user=user).order_by('-pub_date')
        serializer = RecipeSerializer(recipes, many=True)
        return Response({'data': serializer.data})

    """
    DELETE:
    Delete a recipe
    ###Params should be sent:
        {
            'id': 1,
        }
    """
    def delete(self, request):
        recipe_id = request.GET.get('id')
        ingredients = Recipe.objects.filter(id=recipe_id)
        ingredients.delete()
        return Response({'status': 'Deleted'})

    """
    POST:
    Creator class
    ###Fileds should be sent:
        {
            'title': Some Text,
            'image': FILE,
            'ingredients':  [],
            ### or
            'ingredients':  1,
            'ingredients':  2,
            'ingredients':  4,
            ...
        }
    + user - ***Will be added automatically***
    """
    def post(self, request):
        recipe = RecipePostSerializer(data=request.data)
        if recipe.is_valid():
            recipe.save(user=request.user)
            return Response({'status': 'Added'})
        else:
            return Response(recipe.errors)

    """
    PUT:
    Editor class
    ###Fileds should be sent:
        {
            'title': Some Text,
            'image': FILE,
            'ingredients':  [],
            ### or
            'ingredients':  1,
            'ingredients':  2,
            'ingredients':  4,
            ...
        }
    """
    def put(self, request):
        recipe_id = request.GET.get('id')
        recipe = Recipe.objects.filter(id=recipe_id).first()
        serializer = RecipePostSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Edited'})
        else:
            return Response({'status': 'Error'})

