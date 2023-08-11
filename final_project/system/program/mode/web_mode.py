import os
import subprocess


# 파일 찾아주는 함수
def find_files(filename, search_path):
    result = []

    # Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            file = os.path.join(root, filename)
            if '3' not in file:
                result.append(file)
    return result[0]

# 파일 주소로 브라우저를 염
def found_file(target_filename, search_root):
    found_path = find_files(target_filename, search_root)

    if found_path:
        print(f"파일을 찾았습니다: {found_path}")
        subprocess.Popen([found_path])
    else:
        print("파일을 찾을 수 없습니다.")

def web_open_program(tsk):
    # 네이버 웨일 브라우저
    if 'naver' in tsk:
        search_root = "C:\\Program Files\\Naver\\Naver Whale\\Application"
        target_filename = "whale.exe"
        found_file(target_filename, search_root)
        text = '네이버 웨일를 엽니다'

    # 크롬 브라우저
    elif 'chrome' in tsk or tsk == 'internet':
        search_root = "C:\\Program Files\\Google\\Chrome\\Application"
        target_filename = 'chrome.exe'
        found_file(target_filename, search_root)
        text = '크롬 브라우저를 엽니다'

    # 마이크로소프트 엣지 브라우저
    elif 'edge' in tsk:
        search_root = r"C:\Program Files (x86)\Microsoft\Edge\Application"
        target_filename = 'msedge.exe'
        found_file(target_filename, search_root)
        text = '마이크로소프트 엣지 브라우저를 엽니다'

    else:
        text = '없는 프로그램 입니다'

    return text