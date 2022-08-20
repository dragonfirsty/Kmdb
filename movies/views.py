from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response, status

from .models import Movie
from .permissions import AdminPermission
from .serializers import MovieSerializer


class MovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:

        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self,request:Request,movie_id: int)-> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie,data=request.data,partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


    def delete(self, request: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response("", status.HTTP_204_NO_CONTENT)
