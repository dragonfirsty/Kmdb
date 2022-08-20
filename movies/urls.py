from django.urls import path

from . import views

urlpatterns = [
    path("movies/?page=2", views.MovieView.as_view()),
    path("movies/<int:movie_id>/",views.MovieDetailView.as_view()),
]