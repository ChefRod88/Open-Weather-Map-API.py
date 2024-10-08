import requests
# Your Open Weather Map API key
api_key = '7b22ebb55a220a063135b6803b729b9c'
city = 'Orlando'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

# construct the full API request URL
params = {
    'q': city,
    'appid': api_key,
    'units': 'metric' # Get the temperature in Celsius
}

# Send the GET request
response = requests.get(base_url, params=params)

# Convert response to JSON format
weather_data = response.json()

if response.status_code == 200:
    print(f"Weather in {city}:")
    print(f"Temperature: {weather_data['main']['temp']} C")
    print(f"Weather: {weather_data['weather'][0]['description']}")
else:
    print("Error", weather_data)