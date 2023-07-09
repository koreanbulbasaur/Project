import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.ehyundai.com/newPortal/DP/FG/FG000000_V.do?branchCd=B00148000'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, features="html.parser")
floors = soup.find_all('h4', attrs={'class':'guide_cont_tit'})

def checkword(word):
    return re.sub(r'\([^()]*\)', '', word)

for idx, floor in enumerate(floors):
    print(floor.get_text())
    brand_names = soup.find('div', attrs={'id':f'tabContentFloor{idx+1}'}).find_all('strong', attrs={'class':'brand'})
    for brand_name in brand_names:
        name = checkword(brand_name.get_text())
        print(name, end=' ')
    print()
    print('-'*100)