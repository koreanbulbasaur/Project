import gtts
import speech_recognition as sr
import pyttsx3

def listen_to_speech():
    # 음성 인식 객체 생성
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("네 말씀하세요.")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # 잡음 제거를 위해 환경 소음 측정
        audio = recognizer.listen(source)  # 마이크로부터 음성 입력 수신

    try:
        text = recognizer.recognize_google(audio, language='ko-KR')  # 음성을 텍스트로 변환 (한국어 설정)
        print("인식된 텍스트:", text)
        return text
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
        return ""
    except sr.RequestError:
        print("Google Speech Recognition 서비스에 접근할 수 없습니다.")
        return ""

def speak_text(text):
    # 음성 합성 객체 생성
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # 음성 속도 설정 (기본값은 200)

    print("출력할 음성:", text)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        input_text = listen_to_speech()
        if input_text.lower() == '종료':  # '종료'라고 말하면 프로그램 종료
            break
        speak_text(input_text)