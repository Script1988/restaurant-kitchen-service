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
]


app_name = "restaurant_service"
