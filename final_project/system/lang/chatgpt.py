import openai
from lang.chatgpt_message import *

# OpenAI API 키 설정
openai.api_key = "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"

def chat_gpt(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat(text)
    )

    assistant_message = response['choices'][0]['message']['content']
    return assistant_message