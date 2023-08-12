import webbrowser

def search_program(query, task='google'):
    text = None

    if task == 'naver':
        webbrowser.open(f'https://search.naver.com/search.naver?query={query}')
        text = f'네이버에서 {query}를 검색합니다'
    elif task == 'bing':
        webbrowser.open(f'https://www.bing.com/search?q={query}')
        text = f'빙에서 {query}를 검색합니다'
    elif task == 'youtube':
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
        text = f'빙에서 {query}를 검색합니다'
    else:
        webbrowser.open(f'https://www.google.com/search?q={query}')
        text = f'구글에서 {query}를 검색합니다'

    if text:
        return text
    else:
        return '다시 한번 말씀해주세요'