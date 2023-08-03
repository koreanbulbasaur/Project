import MeCab

text = "1시간 알람 맞쳐줘"
text1 = '바탕화면에 있는 PPT 파일 켜줘'

mecab = MeCab.Tagger()
out = mecab.parse(text1)
print(out)