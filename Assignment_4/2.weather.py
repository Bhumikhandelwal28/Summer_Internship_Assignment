#Application programming Interface

import requests
data={
  "coord": {"lon": 73.4017,
    "lat": 18.7549
  },
  "weather": [
    {
      "id": 804,
      "main": "Clouds",
      "description": "overcast clouds",
      "icon": "04d"
    }
  ],
  "base": "stations",
  "main": {
    "temperature": 299.5,
    "feels_like": 299.5,
    "temp_min": 299.5,
    "temp_max": 299.5,
    "pressure": 1007,
    "humidity": 80,
    "sea_level": 1007,
    "grnd_level": 956
  },
  "visibility": 10000,
  "wind": {
    "speed": 6.84,
    "deg": 240,
    "gust": 11.04
  },
  "clouds": {
    "all": 95
  },
  "dt": 1750653997,
  "sys": {
    "country": "IN",
    "sunrise": 1750638649,
    "sunset": 1750686374
  },
  "timezone": 19800,
  "id": 1266666,
  "name": "Lonavala",
  "cod": 200
}


def weather(city,api_key):
    url="https://api.openweathermap.org/data/2.5/weather?"
    final_url=f"{url}q={city}&appid={api_key}&units=metric"
    try:
         response = requests.get(final_url)
         response.raise_for_status()
         data = response.json()

         temperature=data["main"]["temp"]
         humidity=data["main"]["humidity"]
         feels_like=data["main"]["feels_like"]
         pressure=data["main"]["pressure"]
         windspeed=data["wind"]["speed"]

         print(f"Weather in {city}:")
         print(f"Temperature:{temperature}C \n(Feels like:{feels_like}C)")
         print(f"Humidity:{humidity}%")
         print(f"Description: {data['weather'][0]['description'].capitalize()}")
         print(f"Pressure: {pressure}")
         print(f"Wind Speed: {windspeed}")


    except requests.exceptions.RequestException as e:
         print(f"Error fetching weather data: {e}")



api_key="85d6beee578296755c0741308f5dbb0c"
city=input("Enter name of city:")
weather(city,api_key)