from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import pandas as pd
from ssl import Options


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()
rl = 'https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1YL21291E&conn_path=I2'

browser.get(rl)

time.sleep(5)

iframes = browser.find_elements(By.TAG_NAME,"iframe")
browser.switch_to.frame(iframes[1])

iframes2 = browser.find_element(By.TAG_NAME,"iframe") 
browser.switch_to.frame(iframes2)

iframe_source = browser.page_source
soup = BeautifulSoup(iframe_source)

Series = []
listCols = ["소재지(시군구)별"]
find_Table = soup.find('table',class_='fontL')
for i in find_Table.findAll('th',class_='colHead-first'):
    listCols.append(i['title'])

Table_Body = find_Table.find('tbody')

for i in Table_Body.findAll('tr'):
    tmp = []
    for j in i.findAll('td'):
        tmp.append(j['title'].replace(",", ""))
    Series.append(tmp)

Edit_df = pd.DataFrame(Series)
Edit_df.columns = listCols
Edit_df.set_index("소재지(시군구)별",inplace= True)
Edit_df.drop(['전국'],inplace=True)
Edit_df[['2019','2020','2021']] = Edit_df[['2019','2020','2021']].astype('Int64') 

print(Edit_df)