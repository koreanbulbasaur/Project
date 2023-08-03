import webbrowser
import os
import fnmatch
import subprocess

# 파일 찾아주는 함수
def find_file(root_dir, filename):
    for root, dirs, files in os.walk(root_dir):
        for file in fnmatch.filter(files, filename):
            return os.path.join(root, file)
    return None

def web(web_name, query=None, search_opt=False, another_program=None):
    if not(search_opt):
        # 크롬 창 열기(google 접속)
        if another_program is None:
            webbrowser.open("https://www.google.com")
        
        elif another_program == 'whale':
            search_root = "C:\\"
            target_filename = "whale.exe"

            found_path = find_file(search_root, target_filename)

            if found_path:
                print(f"파일을 찾았습니다: {found_path}")
                subprocess.Popen([found_path])
            else:
                print("파일을 찾을 수 없습니다.")


    else:
        # 구글 검색
        if web_name == 'goggle':
            search_url = f"https://www.{web_name}.com/search?q={query}"

        # 네이버 검색
        elif web_name == 'naver':
            search_url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}'

        # bing 검색
        elif web_name == 'bing':
            search_url = f'https://www.bing.com/search?q={query}&ghc=1&lq=0&pq=wef&sc=10-3&qs=n&sk=&cvid=9ED6554057014E0DB9AC9DA723C62EF3&ghsh=0&ghacc=0&ghpl='
        
        # 다음 검색
        elif web_name == 'daum':
            search_url = f'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={query}'

        webbrowser.open(search_url)

web('daum', query='test', search_opt=True)