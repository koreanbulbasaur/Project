from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from time import *
import pandas as pd
from ssl import Options


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = 'https://jumin.mois.go.kr/'

sleep(1)
browser.get(url)

iframe = browser.find_element(By.TAG_NAME,"iframe")
browser.switch_to.default_content()
browser.switch_to.frame(iframe)

iframe_source = browser.page_source
#print(iframe_source) #returns iframe source
#print(browser.current_url) #returns iframe URL

soup = BeautifulSoup(iframe_source)

def Sellect_Option(InputValue1,InputValue2):
    select_elements = browser.find_elements(By.ID,InputValue1) 
    
    for select_element in select_elements:
        select = Select(select_element)
        options = select.options
        
        for option in options:
            if option.get_attribute("value") == InputValue2:
                option.click()
                break


Sellect_Option("searchYearStart","2022")
Sellect_Option("searchMonthStart","12")
Sellect_Option("searchYearEnd","2022")
Sellect_Option("searchMonthEnd","12")

button_element = browser.find_element(By.CLASS_NAME,'btn_search')
button_element.click()

series = []
cols = []

tmp = soup.find('div',class_='dataTables_scrollBody').find('tbody')
for i in tmp.findAll('tr'):
    tmplist = []
    tmplist.append(i.find('td',class_='td_admin th1').get_text())
    for j in i.findAll('td',class_=''):
        readData = j.get_text().replace(" ", "")
        tmplist.append(readData.replace(",", ""))
    series.append(tmplist)

for i in soup.findAll('div',class_='dataTables_sizing'):
    cols.append(i.get_text().replace(" ", ""))

del cols[0]
del cols[1]

df = pd.DataFrame(series)
df.columns = cols

df = df.set_index('행정기관')
df_Edit = df.loc[:,['총인구수']]

df_Edit['총인구수'] = df_Edit['총인구수'].astype('int')