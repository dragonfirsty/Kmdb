from django.shortcuts import get_list_or_404, get_object_or_404
from movies.models import Movie
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from .models import Review
from .permissions import IsAdmin_CriticOrReadOnlyPermission
from .serializers import ReviewSerializer,ReviewPostSerializer


class ReviewView(APIView,PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin_CriticOrReadOnlyPermission]

    def get(self, request: Request, movie_id: int) -> Response:
        reviews = get_list_or_404(Review, movie=movie_id)
        result_page = self.paginate_queryset(reviews, request, view=self)
        serializer = ReviewSerializer(reviews, many=True)

        return self.get_paginated_response(serializer.data)


    def post(self, request: Request, movie_id: int) -> Response:

        serializer = ReviewPostSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(movie_id=movie_id,user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class ReviewDetailView(APIView,PageNumberPagination):
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
