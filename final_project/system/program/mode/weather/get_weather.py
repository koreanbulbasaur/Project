import requests
from program.mode.weather.get_loc import where
from program.mode.weather.get_time import get_date, get_tim
from program.mode.weather.weather_id import *
from program.mode.weather.get_today_weather import today_weather

def find_weather(tim, dat, loc):
    API_KEY = '19c3e32076dde8ae7009a7f9e463cdc5'  # 여기에 API 키를 입력하세요
    lat, lon = where(loc)
    if dat == 'today':
        weather_data = today_weather(loc)
        return False, weather_data
    else:
        error, date = get_date(dat)
    if error:
        return error, weather_data
    time = get_tim(tim)
    date_time = date + ' ' + time

    BASE_URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    response = requests.get(BASE_URL)
    datas = response.json()
    weather_data = {}

    for data in datas['list']:
        if data['dt_txt'] == date_time:
            weather_data['날짜'] = dat
            weather_data['장소'] = loc
            weather_data['평균기온'] = data['main']['temp']
            weather_data['최고기온'] = temp_min_max('max', datas, date)
            weather_data['최소기온'] = temp_min_max('min', datas, date)
            weather_data['체감온도'] = data['main']['feels_like']
            weather_data['기압'] = data['main']['pressure']
            weather_data['습도'] = data['main']['humidity']
            id = data['weather'][0]['id']
            weather_data['날씨상태'] = weatherDescKo[id]
            weather_data['비올확률'] = data['pop']

    return error, weather_data

def temp_min_max(value, datas, date):
    temp_list = []
    if value == 'max':
        for data in datas['list']:
            if date in data['dt_txt']:
                temp_list.append(data['main']['temp_max'])
        temp = max(temp_list)
    else:
        for data in datas['list']:
            if date in data['dt_txt']:
                temp_list.append(data['main']['temp_min'])
        temp = min(temp_list)
    return temp