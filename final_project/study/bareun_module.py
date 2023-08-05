import bareunpy as br
tagger = br.Tagger(apikey="koba-6E3IGSQ-IGKEXXY-SHLTV4Y-ZUDMIAI", domain="custom")

while 1:
    text = str(input())

    print(tagger.pos(text))
    print(tagger.morphs(text))
    print(tagger.nouns(text))
    print(tagger.verbs(text))

# from googletrans import Translator

# def translate_korean_to_english(verb):
#     translator = Translator()
#     translated = translator.translate(verb, src='ko', dest='en')
#     return translated.text

# korean_verb = '열'
# english_verb = translate_korean_to_english(korean_verb)
# print(f"한국어 동사 '{korean_verb}'의 영어 번역: {english_verb}")