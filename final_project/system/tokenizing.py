# from mecab import MeCab
# from pprint import pprint

# mecab = MeCab()

# text = '1시간 알람 맞쳐줘'
# text = '1시에 알람 맞쳐'

# pprint(mecab.pos(text))

from nltk import word_tokenize, pos_tag, ne_chunk

sen = "1시간 알람 맞쳐줘"
tokenized_sen = pos_tag(word_tokenize(sen))
print(tokenized_sen)