from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ['id', 'name', 'direction', 'phone']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField('encode_thumbnail')
    ingredients = serializers.SerializerMethodField('get_ingredients')

    def encode_thumbnail(self, recipe):
        with open(os.path.join(settings.MEDIA_ROOT, recipe.thumbnail.name), "rb") as image_file:
            return base64.b64encode(image_file.read())

    def get_ingredients(self, recipe):
        try:
            recipe_ingredients = models.Ingredient.objects.filter(recipe__id=recipe.id)
            return IngredientSerializer(recipe_ingredients, many=True).data
        except models.Ingredient.DoesNotExist:
            return None

    def create(self, validated_data):

        ingredients_data = validated_data.pop("ingredients")

        restaurant = models.Restaurant.objects.get(pk=validated_data["restaurant_id"])
        validated_data["restaurant"] = restaurant
        recipe = models.Recipe.objects.create(**validated_data)

        # Assign ingredients if they are present in the body
        if ingredients_data:
            for ingredient_dict in ingredients_data:
                ingredient = models.Ingredient(name=ingredient_dict["name"])
                ingredient.save()
                ingredient.recipe.add(recipe)
        return recipe

    class Meta:
        model = models.Recipe
        fields = ['id', 'name', 'type', 'thumbnail', 'ingredients']
