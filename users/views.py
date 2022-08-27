from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from rest_framework.exceptions import PermissionDenied
from .models import User
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
from rest_framework.pagination import PageNumberPagination

class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        user = serializer.data

        password = user.pop("password")

        return Response(user, status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if user:

            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status.HTTP_200_OK)

        return Response(
            {"detail": "invalid username or password"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ListUsersAdminView(APIView,PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self, request: Request) -> Response:
        user = User.objects.all()
        result_page = self.paginate_queryset(user, request, view=self)
        serializer = UserSerializer(result_page, many=True)


        return self.get_paginated_response(serializer.data)


class UserView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        serializer = UserSerializer(user)
        
        if request.user.id != user_id and request.user.is_superuser == False:
            raise PermissionDenied({"detail" :"You do not have permission to perform this action."},403)
        

        return Response(serializer.data, status.HTTP_200_OK)
