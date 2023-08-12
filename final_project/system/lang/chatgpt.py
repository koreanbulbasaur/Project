import openai
from lang.chatgpt_message import *

def chat_gpt(text, openai_key):
    # OpenAI API 키 설정
    openai.api_key = openai_key

    # Chatgpt 에게 역할 부여
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat(text)
    )

    # chatgpt의 대답
    assistant_message = response['choices'][0]['message']['content']
    return assistant_message