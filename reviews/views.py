from django.shortcuts import get_list_or_404, get_object_or_404
from movies.models import Movie
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response, status

from .models import Review
from .permissions import IsAdmin_CriticOrReadOnlyPermission
from .serializers import ReviewSerializer


class ReviewView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin_CriticOrReadOnlyPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        reviews = get_list_or_404(Review, movie=movie_id)

        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request, movie_id: int) -> Response:
        request.data['movie'] = movie_id
        serializer = ReviewSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.movie = movie_id
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class ReviewDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin_CriticOrReadOnlyPermission]

    def get(self, request: Request, movie_id: int, review_id: int) -> Response:
        reviews = get_list_or_404(Review, movie=movie_id)

        review = get_object_or_404(reviews, id=review_id)

        serializer = ReviewSerializer(review)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int, review_id: int) -> Response:
        reviews = get_list_or_404(Review, movie=movie_id)

        review = get_object_or_404(reviews, id=review_id)

        review.delete()

        return Response("", status.HTTP_204_NO_CONTENT)
