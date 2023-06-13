from django.contrib.auth import authenticate
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer


class SignupView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(type=openapi.TYPE_OBJECT,
                                       properties={
                                           "username": openapi.Schema(type=openapi.TYPE_STRING,
                                                                      max_length=255),
                                           "email": openapi.Schema(type=openapi.TYPE_STRING,
                                                                   max_length=255)}),
                "password": openapi.Schema(type=openapi.TYPE_STRING, max_length=255),
                'designation': openapi.Schema(type=openapi.TYPE_STRING, max_length=255)
            }
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'user': openapi.Schema(type=openapi.TYPE_OBJECT,
                                           properties={"id": openapi.Schema(type=openapi.TYPE_INTEGER, max_length=255),
                                                       "username": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                  max_length=255),
                                                       "email": openapi.Schema(type=openapi.TYPE_STRING,
                                                                               max_length=255)}),
                    'photo': openapi.Schema(type=openapi.TYPE_FILE, max_length=255),
                    'designation': openapi.Schema(type=openapi.TYPE_STRING, max_length=255)
                }
            ),
            500: "Internal Server error"
        }

    )
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING, max_length=255),
                'password': openapi.Schema(type=openapi.TYPE_STRING, max_length=255)
            }
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING, max_length=255),
                    'token': openapi.Schema(type=openapi.TYPE_STRING, max_length=255)
                }
            ),
            500: "Internal Server error"
        }

    )
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'Login successfully', 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'email or password is not valid'}, status=status.HTTP_404_NOT_FOUND)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'user': openapi.Schema(type=openapi.TYPE_OBJECT,
                                           properties={"id": openapi.Schema(type=openapi.TYPE_INTEGER, max_length=255),
                                                       "username": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                  max_length=255),
                                                       "email": openapi.Schema(type=openapi.TYPE_STRING,
                                                                               max_length=255)}),
                    'photo': openapi.Schema(type=openapi.TYPE_FILE, max_length=255),
                    'designation': openapi.Schema(type=openapi.TYPE_STRING, max_length=255)
                }
            ),
            500: "Internal Server error"
        }

    )
    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            print(profile)
            data = self.serializer_class(profile)
            return Response(data.data)

        except Exception as e:
            return Response(e, status=404)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(type=openapi.TYPE_OBJECT,
                                       properties={
                                           "username": openapi.Schema(type=openapi.TYPE_STRING,
                                                                      max_length=255),
                                           "email": openapi.Schema(type=openapi.TYPE_STRING,
                                                                   max_length=255)}),
                "password": openapi.Schema(type=openapi.TYPE_STRING, max_length=255),
                'designation': openapi.Schema(type=openapi.TYPE_STRING, max_length=255)
            }
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'user': openapi.Schema(type=openapi.TYPE_OBJECT,
                                           properties={"id": openapi.Schema(type=openapi.TYPE_INTEGER, max_length=255),
                                                       "username": openapi.Schema(type=openapi.TYPE_STRING,
                                                                                  max_length=255),
                                                       "email": openapi.Schema(type=openapi.TYPE_STRING,
                                                                               max_length=255)}),
                    'photo': openapi.Schema(type=openapi.TYPE_FILE, max_length=255),
                    'designation': openapi.Schema(type=openapi.TYPE_STRING, max_length=255)
                }
            ),
            500: "Internal Server error"
        }

    )
    def post(self, request):
        try:
            image = request.FILES['image_test']
            profile = Profile.objects.get(user=request.user)
            profile.photo = image
            profile.save()
            print(profile)
            data = self.serializer_class(profile)
            return Response(data.data)

        except Exception as e:
            return Response(e, status=404)
