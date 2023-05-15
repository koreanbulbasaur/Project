import requests
from bs4 import BeautifulSoup

url = 'https://www.genie.co.kr/chart/top200'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# HTTP GET Request
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')

# 해당 페이지에서 테이블 엘리먼트를 찾아 저장
table = soup.find('table', {'class': 'list-wrap'})

# 테이블 상단에서 제목 행 따로 저장
thead = table.find('thead')

# tbody 태그 바로 아래의 모든 tr 태그 검색
tbody = table.find('tbody')
rows = tbody.find_all('tr')

# 데이터 출력
for row in rows:
    title_td = row.find('td', {'class': 'info'})
    title = title_td.find('a').text.strip()
    artist = title_td.find('a', {'class': 'artist'}).text.strip()

    # 'rank' 제목은 hidden 속성으로 숨겨져 있어, nth-of-type(n+1) selector로 선택
    rank = row.select_one('td.number').text.split()[0]

    print(f'{rank}: {title} - {artist}')
