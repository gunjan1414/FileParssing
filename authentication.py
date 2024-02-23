import requests
from requests.auth import HTTPBasicAuth
import json

base_url = 'https://gorest.co.in/'
username = 'abc'
password = 'abc123'

def authenticate_user(username, password, base_url):
    auth_data = {
        'email': username,
        'password': password
    }
    response = requests.post(f"{base_url}/auth/login", data=auth_data)
    if response.status_code == 200:
        return response.json().get('data').get('access_token')
    else:
        raise Exception("Authentication failed")

