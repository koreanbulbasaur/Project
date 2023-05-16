# 이번 강의는 원래 페이지가 변경 되어 안됨

from ssl import Options
from selenium import webdriver

# 크롬창을 띄우지 않고 작업함
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://jumin.mois.go.kr/"
browser.get(url)

