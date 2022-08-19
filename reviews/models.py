from django.db import models


class RecomendationChoices(models.TextChoices):
    Must_Watch = "Must Watch"
    Should_Watch = "Should Watch"
    Avoid_Watch = "Avoid Watch"
    DEFAULT = "No Opinion"


class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(blank=True, default=False)
    recomendation = models.CharField(
        max_length=50,
        choices=RecomendationChoices.choices,
        default=RecomendationChoices.DEFAULT,
    )

    movie = models.ForeignKey(
        "movies.movie", on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(
        "users.user", on_delete=models.CASCADE, related_name="reviews"
    )
