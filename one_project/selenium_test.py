from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import re
from openpyxl import Workbook

def Select_Option(InputValue1, InputValue2):
    select_element = browser.find_element(By.CLASS_NAME, InputValue1)

    # select 요소를 클릭하여 옵션들을 펼칩니다.
    select_element.click()

    # 클릭할 옵션을 찾아서 클릭합니다.
    option_element = browser.find_element(By.XPATH, f"//select[@class='{InputValue1}']/option[text()='{InputValue2}']")
    option_element.click()

def id_click(id_value):
    id_btn = browser.find_element(By.ID, id_value)
    id_btn.click()

def get_table(n):
    sleep(0.5)
    row_data = []
    # 테이블 요소 찾기(내용)
    table = browser.find_element(By.ID, 'protable')
    row_tbody = table.find_element(By.TAG_NAME, 'tbody')
    rows = row_tbody.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        row_data = [cell.text for cell in cells]
        table_data.append(row_data)
        sheet1.append(row_data)

# 새로운 워크북 생성
workbook = Workbook()

# 시트 선택 (기본 시트인 Sheet 선택)
sheet1 = workbook.active
sheet1.title = '출근'

sheet2 = workbook.create_sheet('퇴근')

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("window-size=1920x1080")

# browser = webdriver.Chrome()
browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = 'https://www.t-money.co.kr/ncs/pct/mtmn/ReadTrprInqr.dev?page=1&rows=10'

browser.get(url)
sleep(3)

# 아이디, 비밀번호 입력
username = browser.find_element(By.ID, 'indlMbrsId')
password = browser.find_element(By.NAME, 'mbrsPwd')

username.send_keys('ga225@naver.com')
password.click()
sleep(1)
password.send_keys('qkekrj0225!')

# 로그인 버튼
id_click('btnLogin')

# 날짜 선택 4월 17일
browser.find_element(By.CLASS_NAME, 'ui-datepicker-trigger').click()

Select_Option('ui-datepicker-month', '4월')

table_element = browser.find_element(By.CLASS_NAME, 'ui-datepicker-calendar')
td_elements = table_element.find_elements(By.TAG_NAME, 'td')

for td_element in td_elements:
    if td_element.text == '17':
        td_element.click()
        break

# 카드 선택
Select_Option('sel_inquiry', '1010-0018-1384-2653 (등록일:2022.03.22 15:50:05)')

sleep(0.5)

# 동의 클릭
id_click('agrmYn1')

# 날짜지정 라디오 선택
id_click('latest06')

# 조회 버튼
id_click('srcBtn')
sleep(0.5)

# 더보기 선택
id_click('inqrDvs2_1')
sleep(2)

# 테이블 요소 찾기(header)
table = browser.find_element(By.ID, 'protable')

table_data_header = []
row_thead = table.find_element(By.TAG_NAME, 'thead')
cells = row_thead.find_elements(By.TAG_NAME, 'th')
row_data = [cell.text for cell in cells]
table_data_header.append(row_data)
sheet1.append(row_data)
sheet2.append(row_data)

# 마지막 페이지 개수 가져오기
last_page = browser.find_element(By.ID, 'inquiryList_div')
a_element = last_page.find_element(By.TAG_NAME, 'a')
text = a_element.get_attribute('innerText')

# 텍스트에서 " / "를 기준으로 분리하고 두 번째 요소를 가져옴
number = int(text.split(" / ")[1])

# 각 페이지 마다 테이블 내용 가져오기
table_data = []
for n in range(1, number + 1):
    print('n :', n)
    if n == 10:
        next_btn = browser.find_element(By.CSS_SELECTOR, "img[alt='다음페이지']")
        next_btn.click()

    get_table(n)

    btn_list = browser.find_element(By.CLASS_NAME, 'paginate')
    a_list = btn_list.find_elements(By.CSS_SELECTOR, 'a')
    for a in a_list:
        a_text = a.get_attribute('innerText')

        if a_text != '':
            a_text = int(a_text)

        if a_text == n + 1 and n > 1:
            print('클릭')
            a.click()
            break

print(table_data)

for i in range(3, 0, -1):
    print(f'{i} second')
    sleep(1)
print('End')

browser.quit()

workbook.save('test.xlsx')