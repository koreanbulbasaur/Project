import webbrowser

def search_program(query, task='google'):
    text = None

    # 네이버에서 검색
    if 'naver' in task:
        webbrowser.open(f'https://search.naver.com/search.naver?query={query}')
        text = f'네이버에서 {query}를 검색합니다'

    # 빙에서 검색
    elif 'bing' in task:
        webbrowser.open(f'https://www.bing.com/search?q={query}')
        text = f'빙에서 {query}를 검색합니다'

    # 유튜브에서 검색
    elif 'youtube' in task:
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
        text = f'빙에서 {query}를 검색합니다'

    # 구글에서 검색
    else:
        webbrowser.open(f'https://www.google.com/search?q={query}')
        text = f'구글에서 {query}를 검색합니다'

    if text:
        return text
    else:
        return '다시 한번 말씀해주세요'