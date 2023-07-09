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
# browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1YL21291E&conn_path=I2'

sleep(0.5)
browser.get(url)

iframe = browser.find_element(By.TAG_NAME, "iframe")
browser.switch_to.default_content()
browser.switch_to.frame(iframe)
browser.switch_to.frame(iframe)

iframe_source = browser.page_source

print(iframe_source)
