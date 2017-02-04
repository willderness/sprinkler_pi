import requests

def get_current_weather():
    # Connecting to the weather api
    url = 'http://api.openweathermap.org/data/2.5/weather?id=4178560&units=imperial&appid=f641b59e03463c808393605f493b1f93'
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    return weather_json

def is_clear_skies(w):
    weather_id = int(w['weather'][0]['id'])
    if weather_id >= 800 and weather_id < 900:
        return True
    else:
        return False


def get_weather_forecast():
    weather_json = get_current_weather()

    # Parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Creating our forecast string
    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'
    
    print(weather_json)
    return forecast
