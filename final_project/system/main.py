from lang.lang_pro import program_str_to_dict
from lang.chatgpt import chat_gpt
from program.main import task_app
import time

openai_key = "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"

def ine_ai(text):
    start = time.time()
    get_text = chat_gpt(text, openai_key)
    print(get_text)
    txt = program_str_to_dict(get_text)
    print(txt)
    talk_text = task_app(txt, openai_key)
    print(talk_text)

    elapsed_time = time.time() - start
    print('time : {:.2f} 초'.format(elapsed_time))

    return(talk_text)