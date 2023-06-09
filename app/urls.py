from .views import UserRegistrationViews, UserLoginViews, ProfilePhotoUploadView
from django.urls import path

urlpatterns = [
    path('register/', UserRegistrationViews.as_view(), name='register'),
    path('login/', UserLoginViews.as_view(), name='login'),
    path('profile/', ProfilePhotoUploadView.as_view(), name='profile'),
]
