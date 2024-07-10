import requests

url = 'https://localhost:44303/CoreWebService.asmx'

try:
    response = requests.get(url, verify=False)
    response.raise_for_status()
    print("Successfully connected to the service")
except requests.exceptions.RequestException as e:
    print(f"Error connecting to the service: {e}")
