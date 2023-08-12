# 역할
chatgpt_role = "당신은 AI 스피커 도우미 입니다. 제가 문장을 보내면 당신은 location, \
    task, action, time, number, date 가 포함되어 있는 단어들이 있다면 영어로 출력해주세요 \
    단 지역명이 포함 되어 있다면 지역명은 한글 그대로 반환해주세요.\
        query 부분은 그대로 반환해주세요."


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

        {"role": "user", "content": '내일 오전 날씨 알려줘'}, 
        {"role": "assistant", "content": "(location : 서울), (task : weather), (action : inform), (date : tomorrow), (time : morning)"},

        {"role": "user", "content": '모레 뒤 날씨를 알려줘'}, 
        {"role": "assistant", "content": "(task : weather), (action : inform), (date : after 2)"},

        {"role": "user", "content": '오늘 날씨'}, 
        {"role": "assistant", "content": "(task : weather), (action : inform), (date : today)"},

        {"role": "user", "content": '주사위 던져줘'}, 
        {"role": "assistant", "content": "(task : dice), (action : roll)"},

        {"role": "user", "content": '1에서 6 중에서 하나만 골라봐'}, 
        {"role": "assistant", "content": "(task : choose), (action : pick), (number : 1-6)"},

        {"role": "user", "content": '동전을 던져줘'}, 
        {"role": "assistant", "content": "(task : coin), (action : flip)"},

        {"role": "user", "content": '유튜브에서 asmr 틀어줘'}, 
        {"role": "assistant", "content": "(task : YouTube), (action : play), (query : asmr)"},

        {"role": "user", "content": ms}
    ]
    return messages

'''
    {"role": "user", "content" : ''}, 
    {"role": "assistant", "content" : ""},
'''