import subprocess
import pyautogui
import time
import pyperclip
import os
import fnmatch

# 파일 찾아주는 함수
def find_file(root_dir, filename):
    for root, dirs, files in os.walk(root_dir):
        for file in fnmatch.filter(files, filename):
            return os.path.join(root, file)
    return None

def window_program(program):
    # 계산기 실행
    if program == 'cal':
        subprocess.run("calc.exe", shell=True)

    # 메모장 실행
    elif program == 'note':
        subprocess.run('notepad.exe', shell=True)

    # 그림판 실행
    elif program == 'paint':
        subprocess.run("mspaint.exe", shell=True)

    # ppt 실행
    elif program == 'ppt':
        search_root = "C:\\"
        target_filename = "POWERPNT.EXE"

        found_path = find_file(search_root, target_filename)
        subprocess.run(found_path)

    # 엑셀 실행
    elif program == 'excel':
        search_root = "C:\\"
        target_filename = "EXCEL.EXE"

        found_path = find_file(search_root, target_filename)
        subprocess.run(found_path)

window_program('excel')