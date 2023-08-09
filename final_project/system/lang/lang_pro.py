from lang.mode import search_text, program_text

class Command:
    def __init__(self, text):
        self.text = text
        self.search_mode = False
        self.program_mode = False
        self.program_string = None
        self.search_string = None
        self.data = {}

    # '검색'이 포함되면 search 모드, 아니면 프로그램 실행 모드
    def text_analyze(self):
        keyword = '검색'
        self.string = None

        if keyword in self.text:
            self.search_string = search_text(self.text)
            self.search_mode = True
        else:
            self.program_string = program_text(self.text)
            self.program_mode = True

    # self.program_string 을 딕셔너리 형태로 바꿈
    def program_str_to_dict(self):
        string = self.program_string
        fields = string.strip('()').split('), (')

        for field in fields:
            key, value = field.split(' : ')
            self.data[key] = value
