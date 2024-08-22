import jwt
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import *
from .utils import Util


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = User.objects.get(email=user_data["email"])
        token = RefreshToken.for_user(user).access_token

        relative_link = reverse("email-verify")
        current_site = get_current_site(request).domain
        
        abs_url = "http://" + current_site + relative_link + "?token=" + str(token)
        email_body = "Hi " + user.username + " Use the link below to verify your email \n" + abs_url
        data = {"email_body": email_body, "email_subject":"Verify Your Email", "to_email":user.email}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmailView(views.APIView):

    serializer_class = VerifyEmailSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="token", 
                description="Description",
                required=False, 
                type=str, 
                location=OpenApiParameter.QUERY
                )])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({"Email": "Successfully activated"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({"Error": "Activation token expired"}, status=status.HTTP_200_OK)
        except jwt.exceptions.DecodeError as identifier:
            return Response({"Error": "Invalid token"}, status=status.HTTP_200_OK)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

