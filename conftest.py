import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


@pytest.fixture()
def user():
    """Create a test user."""
    return User.objects.create_user(
        username="testuser",
        email="user@test.com",
        password="testpass",
    )


@pytest.fixture()
def group():
    """Create a test group."""
    return Group.objects.create(name="testgroup")
