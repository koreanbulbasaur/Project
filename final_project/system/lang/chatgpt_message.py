chatgpt_role = "당신은 AI 스피커 도우미 입니다. 제가 문장을 보내면 당신은 location, \
    task, action, time, number 가 포함되어 있는 단어들이 있다면 영어로 출력해주세요. 날씨를 알려줄때는 location을 한국어 그대로 알려주세요"

'''
    {"role": "user", "content": ''}, 
    {"role": "assistant", "content": ""},
'''

def chat(ms):
    messages=[
        {"role": "system", "content": chatgpt_role},

        # 규칙
        {"role": "user", "content": '바탕 화면에 있는 피피티를 켜줘'}, 
        {"role": "assistant", "content": "(location : desktop), (task : ppt), (action : open)"},

        {"role": "user", "content": '날씨를 알려줘'}, 
        {"role": "assistant", "content": "(task : weather), (action : inform), (time : today)"},

        {"role": "user", "content": '메모장 켜줘'}, 
        {"role": "assistant", "content": "(task : notepad), (action : open)"},

        {"role": "user", "content": '화면 밝기 0으로 해줘'},
        {"role": "assistant", "content": "(task : brightness), (action : set), (number : 0)"},

        {"role": "user", "content": '볼륨 조금 줄여줘'}, 
        {"role": "assistant", "content": "(task : volume), (action : set), (number : a little)"},

        {"role": "user", "content": '소리 꺼줘'}, 
        {"role": "assistant", "content": "(task : volume), (action : set), (number : 0)"},

        {"role": "user", "content": '오늘 서울 날씨 알려줘'}, 
        {"role": "assistant", "content": "(location : 서울), (task : weather), (action : inform), (time : today)"},

        {"role": "user", "content": ms}
    ]
    return messages