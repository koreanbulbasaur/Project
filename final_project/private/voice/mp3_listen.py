from pathlib import Path
from playsound import playsound

folder = Path("./result_audio") # 폴더 경로를 입력하세요
wav_files = folder.glob("*.wav") # 폴더 안의 wav파일들을 찾습니다

wrong_file = []

for file in wav_files: # 파일 목록을 순회합니다
    print(file)
    try:
        playsound(file) # 파일을 재생합니다
    except:
        wrong_file.append(file)

print(wrong_file)