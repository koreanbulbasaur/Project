city_en = ['Heung-hai', 'Reisui', 'Enjitsu', 'Neietsu', 'Eisen', 'Reiko', 'Yong-dong', 'Eisen', 'yeoncheongun', 'Yeoju', 'Yesan', 'Yangsan', 'Yangpyong', 'Yangju', 'Yanggu', 'Wonju', 'Wanju', 'Waegwan', 'Ulsan', 'Vijongbu', 'Tangjin', 'Taesal-li', 'Daejeon', 'Daegu', 'Taisen-ri', 'Taebaek', 'Suigen', 'Sunchun', 'Seoul', 'Suisan', 'Jenzan', 'Songwon', 'Sogcho', 'Sangju', 'Santyoku', 'Fuyo', 'Busan', 'Bucheon', 'Puan', 'Beolgyo', 'Hoko', 'Osan', 'Asan', 'ogcheongun', 'Kosong', 'Nonsan', 'Nangen', 'Naju', 'Munsan', 'Mungyeong', 'Moppo', 'Miryang', 'Masan', 'Keizan', 'Kyonju', 'Kwangyang', 'Kwangju', 'Gwangju', 'Kurye', 'Kuri', 'Kunwi', 'Kunsan', 'Kinzan', 'Kumi', 'Goyang', 'Goseong', 'Kongju', 'Kyosai', 'Koesan', 'Kochang', 'Kimje', 'Kimhae', 'Gimcheon', 'Kijang', 'Gapyeong', 'Kang-neung', 'Kanghwa', 'Iksan', 'Incheon', 'Imsil', 'Ichon', 'Hwasun', 'Hwaseong', 'Hwacheon', 'Hongsung', 'Hongchon', 'Hayang', 'Haenam', 'Chuncheon', 'Jeonju', 'Cheongsong gun', 'Cheongju', 'Tenan', 'Chinju', 'Chinhae', 'Chinchon', 'jin-angun', 'Jeju', 'Changwon', 'Changsu', 'Anyang', 'Anseong', 'Ansan', 'Andong', 'Gaigeturi', 'Sinhyeon', 'Yonmu', 'Tonghae', 'Pubal', 'Seongnam', 'Hanam', 'Hwado', 'Yanggok', 'Ungsang', 'Wabu', 'Naeso', 'Hwawon', 'Kwangmyong', 'Sinan', 'Changnyeong']
city_kr = []

import os
from googleapiclient.discovery import build

os.environ['GOOGLE_API_KEY'] = 'AIzaSyBZ-JL8XVJVBUBdDHOaE6NSf-vaE0NoCIQ'
API_KEY = os.environ['GOOGLE_API_KEY']

translate_client = build('translate', 'v2', developerKey=API_KEY)

def trans(text):
    translation = translate_client.translations().list(
        q=text,
        target='ko',
        key=API_KEY
    ).execute()
    return translation['translations'][0]['translatedText']

for city in city_en:
    trans_city = trans(city)
    city_kr.append(trans_city)

city_dict = [{'city_en':en, 'city_kr': kr}for en, kr in zip(city_en, city_kr)]

print(city_dict)