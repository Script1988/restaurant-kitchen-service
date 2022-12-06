import os
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


def dish_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance)}-{uuid.uuid4()}.{extension}"

    return os.path.join("dishes/", filename)


class Dish(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    # image = models.ImageField(upload_to=dish_image_file_path, null=True, blank=True)
    image = models.ImageField(upload_to="static/dishes/", null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dish_type"
    )
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cook")

    class Meta:
        ordering = ["dish_type"]

    def __str__(self):
        return f"{self.name}, price: {self.price}"
