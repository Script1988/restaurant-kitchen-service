# Generated by Django 4.1.3 on 2022-11-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant_service", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"ordering": ["dish_type"]},
        ),
        migrations.AlterField(
            model_name="dish",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]
