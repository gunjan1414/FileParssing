import pytest
from authentication import authenticate_user
from user_profile import get_user_profile, update_user_profile

@pytest.fixture
def auth_token():
    return authenticate_user("username", "password", "https://gorest.co.in")

def test_get_user_profile(auth_token):
    profile = get_user_profile(auth_token, "https://gorest.co.in")
    assert profile is not None

def test_update_user_profile(auth_token):
    assert update_user_profile(auth_token, "https://gorest.co.in", "New Name") == 200
