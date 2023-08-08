from urllib.parse import urlencode, unquote
import requests
import json

#아래의 공공데이터 링크에서 동네예보와 초단기실황 등 api 가이드를 다운받을수 있습니다.

#이 코드는 초단기 실황을 가져오는 api를 이용했습니다.

# https://www.data.go.kr/data/15084084/openapi.do


# 아래의 링크를 통해 실제 json파일 확인가능, 기상정보 api는 최근1일간의 데이터만 제공하므로 base_date 에는
# 현재날짜로 변경해야 제대로 값을 가져옴,인증키 부분에는 공공데이터 포털에서 신청한 인증키를 입력해야함

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
params ={
        "serviceKey" : unquote("IdvCYmvxjaXivD8ncjsz7vxjLrofEeX9rp9wXAe35FnROYZBbvkmvNZWpeq5shwuB39zmeyMQfI37EC4sSqmEQ=="),

        "base_date" : "20230808",

        "base_time" : "0200",

        "fcstDate": "20230808",

        "fcstTime": "0600",

        "category" : "TMN",

        "numOfRows" : "1",

        "pageNo" : 1,

        "dataType" : "JSON",

        "nx" : 55,

        "ny" : 127,
        }

print(url+"?"+urlencode(params))

response = requests.get(url, params=params)


weather_data = json.loads(response.content)

current_weather = weather_data['response']["body"]["items"]['item'][0]
print(current_weather)

# print(current_weather["fcstDate"])
# print(current_weather["fcstTime"])
# print(current_weather["tmn"])
# print(current_weather["tmx"])