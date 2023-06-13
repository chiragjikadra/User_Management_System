```
## Django API

This project implements a Django REST Framework (DRF) API for user signup, login, and profile management.
It includes views for signing up a user, logging in with authentication, and managing user profiles.

## Installation:

1. Clone the repository:
```

git clone https://github.com/chiragjikadra/User_Management_System

```markdown
2. Create a virtual environment and activate it:
```

python3 -m venv venv

source venv/Script/activate

```markdown
3. Install the dependencies:
```

pip install -r requirements.txt

```markdown
4. Apply database migrations:
```

python manage.py migrate

```markdown
## Usage

To start the Django development server, run the following command:
```

python manage.py runserver

```csharp

By default, the server will start at `http://localhost:8000/`.

## Signup

To sign up a new user, make a POST request to `/signup/` with the following JSON payload:

```json
{
    "user":{
        "username":"chirag",
        "email": "chirag@abc.com",
        "password": "1205"

    },
    "designation":"developer"
}
```

This will create a new user and associated profile.

### Login

To authenticate a user and obtain an authentication token, make a POST request to /login/ with the following JSON
payload:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

### Profile

The profile management endpoints require authentication. Include the obtained token in the Authorization header of the
request:

```makefile
Authorization: Token <token>
```

Get Profile
To retrieve the profile for the currently authenticated user, make a GET request to /profile/.

The response will include the user's profile details.

Update Profile
To update the user's profile picture, make a POST request to /profile/ with a multipart/form-data payload containing an
image file with the field name image_test.

### Tests

To run the tests, use the following command:

```bash
python manage.py test
```
