import requests


def get_user_profile(token, base_url):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f"{base_url}/user/profile", headers=headers)
    return response.json()


def update_user_profile(token, base_url, new_display_name):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    data = {
        'name': new_display_name
    }
    response = requests.put(f"{base_url}/user/profile", headers=headers, data=data)
    return response.status_code


# error_handling.py
def handle_error(response):
    if response.status_code == 401:
        raise Exception("Unauthorized: Token is invalid or expired")
    elif response.status_code == 404:
        raise Exception("Resource not found")

