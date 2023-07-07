import requests
import datetime
from config import WEATHER_TOKEN


def get_weather(city: str) -> str:
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric'
        )

        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        return ''.join([
            f'Погода в городе {city}\nтемпература: {cur_weather} град.Цельсия\n',
            f'влажность: {humidity}\nдавление: {pressure}\n',
            f'время восхода Солнца: {sunrise_timestamp}',
        ]
        )
    except Exception as ex:
        print(ex)
        return 'Check name of city'


def main():
    city = input('Введите название города: ')
    result = get_weather(city)
    print(result)


if __name__ == '__main__':
    main()
