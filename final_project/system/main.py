from lang.lang_pro import program_str_to_dict
from lang.chatgpt import chat_gpt
from program.main import task_app
import time

# openai 키
openai_key = "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"

def ine_ai(text):
    # 프로그램 시작 시간
    start = time.time()

    # 문장 분리
    # location, task, action, time, number, date
    get_text = chat_gpt(text, openai_key)
    print(get_text)

    # 분리된 문장을 dictionary 형태로 변환
    txt = program_str_to_dict(get_text)
    print(txt)

    # 프로그램 실행
    talk_text = task_app(txt, openai_key)
    print(talk_text)

    # 프로그램이 실행된 시간 출력
    elapsed_time = time.time() - start
    print('time : {:.2f} 초'.format(elapsed_time))

    return(talk_text)

while 1:
    txt = input('user : ')
    final = ine_ai(txt)
    print(final)