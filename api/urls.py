from django.urls import include, path
from . import views

urlpatterns = [
    path('restaurants', views.Restaurants.as_view()),
    path('restaurants/<str:restaurant_id>/', views.RestaurantDetail.as_view()),

    path('restaurants/<str:restaurant_id>/recipes/', views.Recipes.as_view()),
    path('restaurants/<str:restaurant_id>/recipes/<str:recipe_id>', views.RecipeDetail.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
