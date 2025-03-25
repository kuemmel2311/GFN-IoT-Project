import requests

# API endpoint
url = "http://localhost:5000/WeatherStationAPI/SendTempData"

# API key
api_key = "d2f8a9c4-3b6e-4f91-a2f7-8e5d1b4a6c3e"

# Headers with API key authentication
headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

# Sample data to send
data = {
    "dataValue": 25.5,
}

# Send POST request
response = requests.post(url, json=data, headers=headers)

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
