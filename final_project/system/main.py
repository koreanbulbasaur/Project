from lang.lang_pro import program_str_to_dict
from lang.chatgpt import chat_gpt
from program.main import task_app
import time

openai_key = "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"

while 1:
    text = input('say something : ')
    start = time.time()
    get_text = chat_gpt(text, openai_key)
    txt = program_str_to_dict(get_text)
    print(txt)
    talk_text = task_app(txt, openai_key)
    print(talk_text)

    elapsed_time = time.time() - start
    print('time : {:.2f} 초'.format(elapsed_time))