from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant_service.forms import CookCreationForm, DishForm, CookExperienceUpdateForm, DishTypeSearchField, \
    DishSearchField, CookSearchField
from restaurant_service.models import DishType, Cook, Dish


def index(request):
    """View function for the home page of the site."""
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_visits": num_visits,

    }

    return render(request, "restaurant_service/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "restaurant_service/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 4
    queryset = DishType.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        context["search_field"] = DishTypeSearchField()

        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)

        return self.queryset


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "restaurant_service/dish_type_detail.html"
    context_object_name = "dish_type_detail"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant_service:dish_type_list")
    template_name = "restaurant_service/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant_service/dish_type_form.html"
    success_url = reverse_lazy("restaurant_service:dish_type_list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "restaurant_service/dish_type_confirm_delete.html"
    success_url = reverse_lazy("restaurant_service:dish_type_list")


class DishListView(generic.ListView):
    model = Dish
    template_name = "restaurant_service/dish_list.html"
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        context["search_field"] = DishSearchField

        return context

    def get_queryset(self):
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)

        return self.queryset


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = DishForm
    success_url = reverse_lazy("restaurant_service:dish_list")
    template_name = "restaurant_service/dish_form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = DishForm
    success_url = reverse_lazy("restaurant_service:dish_list")
    template_name = "restaurant_service/dish_form.html"
    queryset = Dish.objects.all().select_related("dish_type")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant_service:dish_list")


class DishDetailView(generic.DetailView):
    model = Dish


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5
    queryset = Cook.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        context["search_field"] = CookSearchField()

        return context

    def get_queryset(self):
        last_name = self.request.GET.get("last_name")

        if last_name:
            return self.queryset.filter(last_name__icontains=last_name)

        return self.queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("cook__dish_type")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("restaurant_service:cook_list")


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookExperienceUpdateForm
    success_url = reverse_lazy("restaurant_service:cook_list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("restaurant_service:cook_list")
