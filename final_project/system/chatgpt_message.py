chatgpt_role = "당신은 AI 스피커 도우미 입니다. 제가 문장을 보내면 당신은 location, \
    task, action, time, number 가 포함되어 있는 단어들이 있다면 영어로 출력해주세요"

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
        {"role": "assistant", "content": "(task : weather), (action : inform)"},

        {"role": "user", "content": '메모장 켜줘'}, 
        {"role": "assistant", "content": "(task : notepad), (action : open)"},

        {"role": "user", "content": '그림판 열어줘'}, 
        {"role": "assistant", "content": "(task : paint), (action : open)"},

        {"role": "user", "content": '화면 밝기 꺼줘'}, 
        {"role": "assistant", "content": "(task : brightness), (action : set)"},

        {"role": "user", "content": 'c드라이브에 있는 엑셀을 열어줘'}, 
        {"role": "assistant", "content": "(location : C:), (task : excel), (action : open)"},

        {"role": "user", "content": '화면 밝기 0으로 해줘'},
        {"role": "assistant", "content": "(action : set), (task : brightness), (number : 0)"},

        {"role": "user", "content": ms}
    ]
    return messages