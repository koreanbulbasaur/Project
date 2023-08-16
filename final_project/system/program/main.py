from program.mode.bright_mode import bright_program
from program.mode.volume_mode import volume_program
from program.mode.web_mode import web_open_program
from program.mode.run_mode import run_program
from program.mode.weather_mode import weather_program
from program.mode.game_mode import game_program
from program.mode.search_mode import search_program


def task_app(data, openai_key):

    # 인터넷창과 컴퓨터 프로그램 실행 단어 모음
    act_open_list = ['open', 'excute']

    # 인터넷 창 여는 프로그램 모음
    web_program = ['naver whale', 'chrome', 'bing']

    # 컴퓨터 프로그램 모음
    program_list = ['cal', 'calculator', 'notepad', 'paint', 'ppt', 'excel', 'word']

    # 게임 리스트
    game_act = ['roll', 'pick', 'flip', 'toss']

    tim = loc = tsk = act = num = dat = que = None
    
    # data 딕셔너리에 있는 키와 값들을 반복문으로 순회
    for key, value in data.items():
        # 값이 존재하면
        if value:
            # 키에 따라서 변수에 값을 할당하고 소문자로 변환
            if key == 'time':
                tim = value.lower()
            elif key == 'location':
                loc = value.lower()
            elif key == 'task':
                tsk = value.lower()
            elif key == 'action':
                act = value.lower()
            elif key == 'number':
                num = value.lower()
            elif key == 'date':
                dat = value.lower()
            elif key == 'query':
                que = value.lower()

    if que:
        # 검색 
        output_text = search_program(que, task=tsk)

    elif act:
        # 정보
        if act == 'inform':
            # 날씨
            if tsk == 'weather':
                if not(tim):
                    tim = 'now'
                if not(loc):
                    loc = '서울'
                if not(dat):
                    dat = 'today'
                output_text = weather_program(tim, dat, loc, openai_key)

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

        # 간단한 게임 실행
        elif act in game_act:
            output_text = game_program(tsk, num)
        else:
            output_text = '학습되지 않은 명령어 입니다'
    else:
        output_text = '다시 한번 말해주세요'

    return output_text