import openai
from chatgpt_message import *

# OpenAI API 키 설정
openai.api_key = "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"

while True:
    user_input = input("User: ")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat(user_input)
    )

    assistant_message = response['choices'][0]['message']['content']
    print(f"Chat GPT: {assistant_message}")
