from program.mode.weather.get_weather import find_weather
import openai

# OpenAI API 키 설정
openai.api_key = "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"
chatgpt_role = '당신은 기상캐스터 입니다. 제가 주는 데이터로 자연스럽게 기상캐스트 처럼 말해보세요. 단 인사는 생략해주세요'

def weather_program(tim, dat, loc):
    if loc is None:
        loc = '서울'
    if dat is None:
        dat = 'today'
    error, get_weather_data = find_weather(tim, dat, loc)
    if error:
        return get_weather_data
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        # 규칙
        {"role": "system", "content": chatgpt_role},
        {"role": "user", "content": str(get_weather_data)}]
    )

    assistant_message = response['choices'][0]['message']['content']
    return assistant_message