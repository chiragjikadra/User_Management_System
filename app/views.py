from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Profile
from .serializers import UserRegistrationSerializer, UserLoginSerializer


# Create your views here.
class UserRegistrationViews(APIView):
    def post(self, request):
        serialiser = UserRegistrationSerializer(data=request.data)
        if serialiser.is_valid(raise_exception=True):
            user = serialiser.save()
            return Response({'message': 'Registration successfully'}, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginViews(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'Login successfully', 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'email or password is not valid'}, status=status.HTTP_404_NOT_FOUND)


class ProfilePhotoUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        print(user)
        profile = Profile.objects.get(user=user)

        photo = request.data.get('photo')
        profile.profile_photo = photo
        profile.save()

        return Response({'message': 'Profile photo uploaded successfully'})
        # if request.method == 'POST':
        #     form = ProfileForm(request.POST, request.FILES, instance=profile)
        #     if form.is_valid():
        #         form.save()
        #         return redirect('profile')
        # else:
        #     form = ProfileForm(instance=profile)
        #
        # return render(request, 'profile.html', {'form': form, 'profile': profile})
