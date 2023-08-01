from gtts import gTTS
from playsound import playsound


# 영어 문장
text = 'Can I help you?'
file_name = 'sample.mp3'

# 문장을 영어로 인식해서 음성으로 바꿈
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)
# playsound(file_name)

# 한글 문장
text = '모델에 대한 하이퍼파라미터는 모델 학습을 위한 설정과 모델 레이어의 차원 수 설정으로 나뉜다.'
tts_kr = gTTS(text=text, lang='ko')
tts_kr.save(file_name)
# playsound(file_name)

with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_en = gTTS(text=text, lang='ko')
tts_en.save(file_name)
playsound(file_name)