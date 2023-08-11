from bs4 import BeautifulSoup as bs
import requests

def today_weather(loc):
    city = loc
    html = requests.get(f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={city}+날씨')

    soup = bs (html.text, 'html.parser')

    # 날씨 상태
    weather = soup.find('span', {'class':'before_slash'}).text
    weather_set = weather

    # 현재 온도
    current_temp = soup.find('div', {'class':'temperature_text'}).text.replace('현재 온도', '').replace('°','')

    # 체감 온도, 강수, 습도 박스
    box1 = soup.find_all('dd', {'class':'desc'})

    # 체감 온도
    human_temp = box1[0].text.replace('°' ,'')

    # 강수량
    rain_weight = box1[1].text.replace('mm', '')

    # 습도
    humidity = box1[2].text.replace('%', '')

    # 미세먼지, 초미세먼지, 자외선박스
    box2 = soup.find_all('li', {'class': 'item_today'})

    # 미세먼지
    pm10 = box2[0].find('span', {'class': 'txt'}).text

    # 초미세먼지
    pm25 = box2[1].find('span', {'class': 'txt'}).text

    # 자외선
    uv = box2[2].find('span', {'class': 'txt'}).text
    gray_weather = ['비', '흐린 날씨', '흐림']

    # 최소 기온
    min_temp = soup.find('span', {'class':'lowest'}).text.replace('최저기온', '').replace('°','')

    # 최대 기온
    max_temp = soup.find('span', {'class':'highest'}).text.replace('최고기온', '').replace('°','')

    weather_dict = {}
    weather_dict['위치'] = city
    weather_dict['날짜'] = '오늘'
    weather_dict['날씨상태'] = weather_set
    weather_dict['현재온도'] = current_temp
    weather_dict['체감온도'] = human_temp
    weather_dict['최소기온'] = min_temp
    weather_dict['최대기온'] = max_temp
    weather_dict['강수량'] = rain_weight
    weather_dict['습도'] = humidity
    if not(weather_set in gray_weather):
        weather_dict['자외선'] = uv
    weather_dict['미세먼지'] = pm10
    weather_dict['초미세먼지'] = pm25

    return weather_dict