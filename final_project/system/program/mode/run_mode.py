import os
import fnmatch
import subprocess

# 파일 찾아주는 함수
def find_file(root_dir, filename):
    for root, dirs, files in os.walk(root_dir):
        for file in fnmatch.filter(files, filename):
            return os.path.join(root, file)
    return None

# 파일 실행
def run_program(tsk):
    text = None
    # 계산기 실행
    if 'cal' in tsk:
        subprocess.Popen(["calc.exe"])
        text = '계산기를'

    # 메모장 실행
    elif 'notepad' == tsk:
        subprocess.Popen(['notepad.exe'])
        text = '메모장을'

    # 그림판 실행
    elif 'paint' in tsk:
        subprocess.Popen(["mspaint.exe"])
        text = '그림판을'

    # ppt 실행
    elif 'ppt' in tsk:
        search_root = r"C:\Program Files\Microsoft Office\root\Office16"
        target_filename = "POWERPNT.EXE"

        found_path = find_file(search_root, target_filename)
        subprocess.Popen([found_path])
        text = '피피티를'

    # 엑셀 실행
    elif 'excel' in tsk:
        search_root = r"C:\Program Files\Microsoft Office\root\Office16"
        target_filename = "EXCEL.EXE"

        found_path = find_file(search_root, target_filename)
        subprocess.Popen([found_path])
        text = '엑셀를'

    # 워드 실행
    elif 'word' in tsk:
        search_root = r"C:\Program Files\Microsoft Office\root\Office16"
        target_filename = "WINWORD.EXE"

        found_path = find_file(search_root, target_filename)
        subprocess.Popen([found_path])
        text = '워드를'

    else:
        sentence = '없는 프로그램입니다'

    if text:
        sentence = f'{text} 실행 하였습니다'

    return sentence
