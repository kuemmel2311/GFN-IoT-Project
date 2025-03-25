import requests

# API endpoint
url = "http://localhost:5000/WeatherStationAPI/SendTempData"

# API key (replace with a valid key)
api_key = "d2f8a9c4-3b6e-4f91-a2f7-8e5d1b4a6c3e"

# Data payload
payload = {
    "DataValue": 30.5  # Replace with actual temperature value
}

# Headers including API key
headers = {
    "accept": "*/*",
    "Content-Type": "application/json",
    "APIKey": api_key
}

# Send POST request
response = requests.post(url, json=payload, headers=headers)

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
