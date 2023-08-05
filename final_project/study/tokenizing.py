import MeCab
while 1:
    text = str(input())
    if text == 'q':
        break
    mecab = MeCab.Tagger()
    out = mecab.parse(text)
    print(out)

text = "1시간 알람 맞쳐줘"
text1 = '바탕화면에 있는 PPT 파일 켜줘'
text2 = '바탕화면에 있는 메모장 켜줘'

mecab = MeCab.Tagger()
out = mecab.parse(text2)
print(out)