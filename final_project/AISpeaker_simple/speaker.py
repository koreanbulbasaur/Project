import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time, os

# 음성 인식 (듣기, STT)
def listen(recoginzer, audio):
    try:
        text = recoginzer.recognize_google(audio, language='ko')
        print('[me] :', text)
        answer(text)

    except sr.UnknownValueError:
        print('인식 실패') # 음성 인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패 {}'.format(e)) # API Key 오류, 네트워크 단절 등

# 대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        answer_text = '오늘의 서울 기온은 20도입니다. 말은 하늘이 예상됩니다.'
    elif '고마워' in input_text:
        answer_text = '별 말씀을요.'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요'
        stop_listening(wait_for_stop=False) # 더 이상 듣지 않음
    else:
        answer_text  = '다시 한 번 말씀해주세요'

    speak(answer_text)

# 소리내어 읽기 (TTS)
def speak(text):
    print('[자비스] :', text)
    file_name = './audio/voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): # voice.mp3 파일 삭제
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)

while True:
    time.sleep(0.1)