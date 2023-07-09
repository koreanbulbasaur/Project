from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import pandas as pd
from ssl import Options

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument("--headless=new")
options.add_argument("window-size=1920x1080")

# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.maximize_window()
rl = 'https://jumin.mois.go.kr/'

time.sleep(1)
browser.get(rl)

iframe = browser.find_element(By.TAG_NAME, "iframe")
browser.switch_to.default_content()
browser.switch_to.frame(iframe)

iframe_source = browser.page_source
# print(iframe_source) #returns iframe source
# print(browser.current_url) #returns iframe URL

select_elements = []

soup = BeautifulSoup(iframe_source)

select_elements = browser.find_elements(By.ID, "searchYearStart")


for i in select_elements:
    select = Select(i)
    select.select_by_value('2022')


for select_element in select_elements:
    select = Select(select_element)
    options = select.options

    for option in options:
        if option.get_attribute("value") == "2022":
            option.click()
            break

selected_option = select.first_selected_option
selected_value = selected_option.get_attribute('value')
selected_text = selected_option.text

print(selected_text)
