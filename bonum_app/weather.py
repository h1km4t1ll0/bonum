import requests


class Weather:
    def __init__(self,
                 token: str,
                 latitude: float,
                 longitude: float):
        self.latitude = latitude
        self.longitude = longitude
        self.token = token

    def get_weather(self):
        return requests.get(f'https://api.openweathermap.org/data/2.5/weather/'
                            f'?lat={self.latitude}&lon={self.longitude}&appid={self.token}&units=metric&lang=ru').json()

    def compile(self):
        weather = self.get_weather()
        return f"На улице {weather['weather'][0]['description']}, " \
               f"температура {weather['main']['temp']}, " \
               f"ощущается как {weather['main']['feels_like']}, " \
               f"ветер {weather['wind']['speed']} м/с"
