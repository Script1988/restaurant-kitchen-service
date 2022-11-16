import math

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from restaurant_service.models import Cook, Dish


class CookCreationForm(UserCreationForm):

    class Meta:
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience", "first_name", "last_name",)

    def clean_years_of_experience(self):
        experience = self.cleaned_data["years_of_experience"]

        if experience < 0:
            raise ValidationError("Experience can not be lower 0 ")

        return math.floor(experience)


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"
