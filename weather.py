import requests



def weather_res(city, country):
    # api_location = "http://ip-api.com/json/?fields=61439"

    # json_data_1 = requests.get(api_location).json()
    # city = json_data_1['city']
    # country = json_data_1['country']

    api_weather = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country + "&units=metric&APPID=<API-KEY>"

    json_data_2  = requests.get(api_weather).json()
    return json_data_2
