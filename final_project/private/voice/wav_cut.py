from pydub import AudioSegment
from end_point_list import *
import os
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

# 폴더의 경로를 지정합니다.
folder_path = "./result_audio"

# 폴더에 있는 모든 파일의 이름을 가져옵니다.
file_names = os.listdir(folder_path)

# 파일들을 삭제합니다.
for file_name in file_names:
    os.remove(os.path.join(folder_path, file_name))

start_time = 0

def transform_number(num):
    if num < 10:
        return num * 100
    elif num < 100:
        return num * 10
    else:
        return num

# 분:초:밀리초 를 밀리초로 변환
def time_to_milliseconds(time_str):
    minutes, seconds = time_str.split(":")
    seconds, milliseconds = seconds.split(".")
    minutes = int(minutes)
    seconds = int(seconds)
    milliseconds = transform_number(int(milliseconds))
    total_milliseconds = (minutes * 60 * 1000) + (seconds * 1000) + milliseconds
    return total_milliseconds

def cut_audio(input_file, output_file, start_time, end_time):
    # 음원 파일 로드
    audio = AudioSegment.from_file(input_file)

    # 음원 자르기
    cut_audio = audio[start_time:end_time]

    # 자른 음원 파일 저장
    cut_audio.export(output_file, format="wav")

# 음원 파일 경로 설정
try:
    input_file = "./kronii_korean_group.mp3"  # 원본 음원 파일 경로

    for i, end_time_point in enumerate(end_point):
        if end_time_point[1] != '':
            # 음원 자르기
            output_file = f"./result_audio/voice_{str(i).zfill(2)}.wav"  # 자른 음원을 저장할 파일 경로
            end_time = time_to_milliseconds(end_time_point[0])
            cut_audio(input_file, output_file, start_time, end_time)
            start_time = time_to_milliseconds(end_point[i][0])
            data = f'voice_{str(i).zfill(2)}.wav', end_point[i][1]
            ws.append(data)
        else:
            start_time = time_to_milliseconds(end_point[i][0])
except Exception as e:
    print(e)

wb.save('test.csv')