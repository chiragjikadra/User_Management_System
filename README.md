Django API

This project implements a Django REST Framework (DRF) API for user signup, login, and profile management.
It includes views for signing up a user, logging in with authentication, and managing user profiles.

Installation:

1.Create a virtual environment and activate it:

2.Install the dependencies:
 - pip install -r requirements.txt

3.Apply database migrations:
-python manage.py migrate

Usage

To start the Django development server, run the following command:
-python manage.py runserver

By default, the server will start at http://localhost:8000/.

Signup
To sign up a new user, make a POST request to /signup/ with the following JSON payload:

{
    "user":
    {
        "username":"example",
        "email": "example@abc.com",
        "password": "example"
    },
    "designation":"developer"
}

This will create a new user and associated profile.

Login
To authenticate a user and obtain an authentication token, make a POST request to /login/ with the following JSON payload:
{
  "email": "user@example.com",
  "password": "password123"
}
If the credentials are valid, the response will include a token that can be used for subsequent authenticated requests.

Profile
The profile management endpoints require authentication. Include the obtained token in the Authorization header of the request:
Authorization: Token <token>
Get Profile
To retrieve the profile for the currently authenticated user, make a GET request to /profile/.

The response will include the user's profile details.

Update Profile
To update the user's profile picture, make a POST request to /profile/ with a multipart/form-data payload containing an image file with the field name image_test.

Tests
To run the tests, use the following command:

bash
python manage.py test
This will execute the test cases and display the results.