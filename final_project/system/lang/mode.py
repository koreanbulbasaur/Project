import openai
from lang.chatgpt_message import *

openai.api_key = "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"

def program_text(text):
    user_input = text

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat(user_input)
    )
    
    assistant_message = response['choices'][0]['message']['content']
    print(f"Assistant: {assistant_message}")
    return assistant_message

# gpt를 이용해서 어디 프로그램에서 뭘 검색 할지 구분
def search_text(text):
    pass