import openai
from chatgpt_message import quest

# open ai에서 발급받은 api key를 등록합니다
OPENAI_YOUR_KEY = "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"
openai.api_key = OPENAI_YOUR_KEY

MODEL = "gpt-3.5-turbo"

while True:
    question = input("Q:")
    if question == '종료' or question == 'exit':
        break

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=quest(question),
        temperature=0,
        prompt=question
        )

    output_text = response["choices"][0]["message"]["content"]
    print(output_text)