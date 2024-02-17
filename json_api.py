import requests
from requests.auth import HTTPBasicAuth
import json

base_url = 'https://gorest.co.in/'
username = 'abc'
password = 'abc123'
data = {'Product ID: 12345': 'Name: Product Name'}, {'Product ID: 12345': 'Price: $19.99'}, {'Product ID: 12345': 'In Stock: Yes'}

class GoRestAPI:
    def __init__(self, base_url, username, password, data):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.data = data
        self.token = None

    def json_api(self):
        try:
            headers = {'Accept': '*/*', "User-Agent": "Apache-HttpClient/4.1.1 (java 1.5)",
                       'Content-Type': 'application/json'}
            response = requests.post(base_url, data=json.dumps(data), headers=headers,
                                     auth=HTTPBasicAuth(username, password), verify=False)
            if response.status_code == 200:
                self.token = response.json().get('data', {}).get('token', None)
                print("Authentication successful.")
            else:
                print("Failed to authenticate.")
                return False
        except Exception as e:
            print(e)


obj = GoRestAPI(base_url, username, password, data)
obj.json_api()