from django.urls import path

from restaurant_service.views import (
    index,
    CookListView,
    DishTypeListView,
    DishListView,
    DishTypeDetailView,
    DishDetailView,
    CookDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookCreateView,
    CookDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish_type_detail"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish_type_form"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish_type_update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish_type_delete"),
    path("dishes/create/", DishCreateView.as_view(), name="dish_create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish_update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish_delete"),
    path("cooks/create/", CookCreateView.as_view(), name="cook_create"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook_delete")
]


app_name = "restaurant_service"
