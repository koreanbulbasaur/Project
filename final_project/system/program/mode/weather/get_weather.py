import requests
from program.mode.weather.get_loc import where
from program.mode.weather.get_time import get_date, get_tim
from program.mode.weather.weather_id import *
from program.mode.weather.get_today_weather import today_weather

def find_weather(tim='now', dat='today', loc='서울'):
    API_KEY = '19c3e32076dde8ae7009a7f9e463cdc5'  # 여기에 API 키를 입력하세요

    # 위치를 위도와 경도로 반환
    lat, lon = where(loc)

    # 날짜가 오늘일 경우 네이버에서 검색함
    if dat == 'today':
        weather_data = today_weather(loc)
        return False, weather_data
    
    # 오늘이 아닌 다른 날은 숫자로 반환
    else:
        error, date = get_date(dat)

    # 4일 뒤의 날씨는 못가져옴
    if error:
        return error, weather_data

    # 시간을 시분초로 반환
    time = get_tim(tim)
    date_time = date + ' ' + time

    # openweathermap에서 날씨 예보 정보를 가져옴
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

# 하루의 최대 기온과 최소 기온을 구하는 함수
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