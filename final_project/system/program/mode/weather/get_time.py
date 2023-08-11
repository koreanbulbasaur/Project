from datetime import datetime, timedelta

def get_date(dat):
    add_date = 0
    date_over = False
    if dat == 'tomorrow':
        add_date = 1
    elif 'after' in dat:
        add_date = int(dat.split()[-1])
        if add_date > 4:
            date_over = True
            return_text = '4일 뒤까지의 날씨 정보만 가져올 수 있습니다. 원하시는 날짜를 확인 후 요청해 주세요.'
            return date_over, return_text

    date_get = (datetime.now() + timedelta(days=add_date)).strftime('%Y-%m-%d')
    return date_over, date_get

def get_tim(tim):
    form_time = datetime.now().hour
    if 'am' in tim or 'pm' in tim:
        form_time = convert_time(tim)
    if tim == 'midnight' or form_time < 3:
        set_time = 0
    elif tim == 'dawn' or form_time < 6:
        set_time = 3
    elif tim == 'dusk' or form_time < 9:
        set_time = 6
    elif tim == 'morning' or form_time < 12:
        set_time = 9
    elif tim == 'noon' or form_time < 15:
        set_time = 12
    elif tim == 'afternoon' or form_time < 18:
        set_time = 15
    elif tim == 'evening' or form_time < 21:
        set_time = 18
    elif tim == 'twilight' or form_time < 24:
        set_time = 21
    return f'{set_time:02d}:00:00'

def convert_time(time_str):
    int_time = datetime.now().hour
    if 'am' in time_str:
        hour = int(time_str.split(' ')[1])
        int_time = hour
        if hour == 12:
            int_time = 0
    elif 'pm' in time_str:
        hour = int(time_str.split(' ')[1])
        if hour != 12:
            hour += 12
        int_time = hour
    return int_time