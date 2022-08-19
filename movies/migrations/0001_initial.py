# Generated by Django 4.1 on 2022-08-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("genres", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(max_length=10)),
                ("premiere", models.DateField()),
                ("classification", models.IntegerField()),
                ("synopsis", models.TextField()),
                (
                    "genres",
                    models.ManyToManyField(related_name="movies", to="genres.genre"),
                ),
            ],
        ),
    ]