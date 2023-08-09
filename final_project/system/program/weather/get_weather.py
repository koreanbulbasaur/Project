import requests
from google_map import where

API_KEY = '19c3e32076dde8ae7009a7f9e463cdc5'  # 여기에 API 키를 입력하세요
lat, lon = where('서울')

BASE_URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(BASE_URL)
data = response.json()
print(data)
# for day in data['daily']:
#     pass