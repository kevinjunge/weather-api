import requests


API_KEY = "4f8e52ca802b3fc52650ef7536bcc744"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# make get request
response = requests.get(request_url)

# check status code
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")

