import pytest
from authentication import authenticate_user

def test_authentication():
    token = authenticate_user("username", "password", "https://gorest.co.in")
    assert token is not None
