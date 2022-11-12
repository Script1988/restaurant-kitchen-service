from django.urls import path

from restaurant_service.views import index


urlpatterns = [
    path("", index, name="index"),
]


app_name = "restaurant_service"
