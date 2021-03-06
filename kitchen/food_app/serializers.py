from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'price')


class RecipeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Recipe
        fields = ('title', 'user', 'ingredients', 'image')


class RecipePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'image')


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ('step_text', 'added', 'recipe')

