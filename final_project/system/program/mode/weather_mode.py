from program.mode.weather.get_weather import find_weather
import openai

chatgpt_role = '당신은 기상캐스터 입니다. 제가 주는 데이터로 자연스럽게 기상캐스트 처럼 말해보세요. 단 인사는 생략해주세요'

def weather_program(tim, dat, loc, openai_key):
    error, get_weather_data = find_weather(tim=tim, dat=dat, loc=loc)

    # 에러 반환
    if error:
        return get_weather_data
    
    # OpenAI API 키 설정
    # 기상캐스터처럼 말함
    openai.api_key = openai_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        # 규칙
        {"role": "system", "content": chatgpt_role},
        {"role": "user", "content": str(get_weather_data)}]
    )

    assistant_message = response['choices'][0]['message']['content']
    return assistant_message