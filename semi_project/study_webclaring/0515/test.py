import requests
from bs4 import BeautifulSoup

# 웹 페이지의 URL
url = 'https://jumin.mois.go.kr/ageStatMonth.do'

# requests 라이브러리를 사용하여 웹 페이지의 HTML을 가지고 옴
response = requests.get(url)

# BeautifulSoup 라이브러리를 사용하여 HTML을 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# HTML에서 <table> 태그를 검색하여 가져옴
tables = soup.find_all('table')

# <table> 태그 안의 내용을 모두 출력
for table in tables:
    print(table)