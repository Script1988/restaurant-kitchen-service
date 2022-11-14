from django.shortcuts import render
from django.views import generic

from restaurant_service.models import DishType, Cook, Dish


def index(request):
    """View function for the home page of the site."""
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,

    }

    return render(request, "restaurant_service/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "restaurant_service/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "restaurant_service/dish_type_detail.html"
    context_object_name = "dish_type_detail"


class DishListView(generic.ListView):
    model = Dish
    template_name = "restaurant_service/dish_list.html"
    queryset = Dish.objects.all().select_related("dish_type")


class DishDetailView(generic.DetailView):
    model = Dish


class CookListView(generic.ListView):
    model = Cook


class CookDetailView(generic.DetailView):
    model = Cook
