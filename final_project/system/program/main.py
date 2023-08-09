from bright_mode import bright_program
from volume_mode import volume_program
from web_mode import web_open_program
from run_mode import run_program
from weather_mode import weather_program

act_open_list = ['open', 'excute']

web_program = ['naver whale', 'chrome', 'bing']
program_list = []

def task_app(data):
    tim = data.get('time').lower()
    loc = data.get('location').lower()
    tsk = data.get('task').lower()
    act = data.get('action').lower()
    num = data.get('number').lower()

    if act:
        # 정보
        if act == 'inform':
            # 날씨
            if tsk == 'weather':
                output_text = weather_program(tim, loc)

        elif act == 'set':
            # 화면 밝기
            if tsk == 'brightness':
                output_text = bright_program(num)

            # 소리 조절
            elif tsk == 'volume':
                output_text = volume_program(num)

        elif act in act_open_list:
            # 인터넷 창 열기
            if tsk in web_program:
                output_text = web_open_program(tsk)

            # 컴퓨터 프로그램 열기
            elif tsk in program_list:
                output_text = run_program(tsk)

    else:
        output_text = '다시 한번 말해주세요'
    
    return output_text