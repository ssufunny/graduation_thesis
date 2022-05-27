import copyreg
import re
import numpy as np
import MeCab
from collections import Counter
import pandas as pd
import os

# text 파일 불러오기
# text 파일 위치(노트북)
# f = open("C://Users//jisu//Desktop//본문수집.txt", 'r', encoding='utf-8')
# text 파일 위치(컴퓨터)
f = open("C://graduation_thesis//graduation_thesis//myfile.txt", 'r', encoding='utf-8')
text_file = f.read()
# Mecab 이용
m = MeCab.Tagger()
# parse 함수 사용(형태소 분석 & 품사 매칭)
texts = m.parse(text_file)
# 띄어쓰기, 줄바꿈마다 split
words = re.split('[\t\n]', texts)

tagging = []
word = []

# 단어와 품사 태깅 부분으로 배열 따로 지정
for i in range(0, len(words) - 1):  # 배열 길이만큼 반복
    if i % 2 == 1:  # 품사 태깅
        tagging.append(words[i])
    else:  # 단어
        if words[i] != "EOS":  # "EOS" 제외한 단어만
            word.append(words[i])

num = -1
place = []
tags = []

# 저장 하지 않을 장소
not_save = ['지역', '국내', '대한민국', '한국', '중심', '장소', '도시', '현장', '해외', '내륙', '외국', '명소', '관광지', '아시아', '우주', '호텔', '마을']

for i in tagging:
    tag, category, TF, read, word_type, first_tag, last_tag, exp = i.split(',')
    num += 1
    name = re.search("[가-힣]+", word[num])   # 한글
    if name:
        if (category == '지명') or (category == '장소'):
            if (word[num] not in not_save):
                place.append(word[num])
                tags.append(tag)
                count = Counter(place)
place_count = []
places = []

for i, j in count.most_common(100):
    if len(i) >= 2:
        places.append(i)
        place_count.append(j)

# 빈도수가 가장 많은 단어
most_place = places[0]
most_place_index = place.index(most_place)
most_place_tag = tags[most_place_index]

# 태그 넣기
place_tags = []
for i in range(len(places)):
    place_tag = tags[place.index(places[i])]
    place_tags.append(place_tag)
count_NNG = place_tags.count('NNG')
count_NNP = place_tags.count('NNP')
# print(place_tags)
# test용 print
for i in range(len(places)):
    print(places[i], place_tags[i], place_count[i])
print(count_NNG, count_NNP)

# 상호명 엑셀 파일 열기
filename = 'C://graduation_thesis//build_list.xlsx'
build_list = pd.read_excel(filename, engine="openpyxl", keep_default_na=False)

addresses = []
with open('address.txt', 'r', encoding='utf-8') as f:
    file_data = f.readlines()
    # print(file_data)
    for i in file_data:
        # address, build = i.split(',')
        addresses.append(i)

# 빈도표로 장소 정보 알아내기
# 빈도표에서 품사가 NNG인 단어를 포함하는 장소 찾기
NNG_place = places[place_tags.index('NNG')]
print(NNG_place)
if NNG_place == '해변' or NNG_place == '해수욕장':
    df_NNG_place = build_list.loc[build_list['Column2'].str.contains('해변|해수욕장')]
elif NNG_place == '터널':
    df_NNG_place = build_list.loc[build_list['Column2'].str.contains('터널|굴')]
else:
    df_NNG_place = build_list.loc[build_list['Column2'].str.contains(NNG_place)]
print(df_NNG_place)
# NNG인 단어를 포함하는 장소의 목록이 1개가 될 때까지 NNP인 단어 함께 검색

index1 = 0
index2 = 0

while (len(df_NNG_place) != 1):
    if -1 < index1 < 10:
        NNP_place = places[place_tags.index('NNP', index1)]
        print(index1, NNP_place)
        df_NNP_place = df_NNG_place.loc[df_NNG_place['Column1'].str.contains(NNP_place)]
        print(df_NNP_place)
        if df_NNP_place.empty:
            df_NNP_place = df_NNG_place.loc[df_NNG_place['Column2'].str.contains(NNP_place)]
            if df_NNP_place.empty:
                df_NNP_place = df_NNG_place
        df_NNG_place = df_NNP_place
        result = df_NNG_place['Column1'] + " " + df_NNG_place['Column2']
        index1 += 1
    # else:
    #     break

# while (len(df_NNG_place) != 1):
    elif index1 == 10 and -1 < index2 < 10:
        NNP_place = places[place_tags.index('NNP', index2)]
        print(index2, NNP_place)
        for j in addresses:
            # print(j)
            if NNP_place in j:
                address, build = j.split(',')
                data = {'Column1': [address], 'Column2': [build[:-1]]}
                df_NNG_place = pd.DataFrame(data)
            else:
                df_NNG_place = df_NNP_place
        index2 += 1
print(df_NNG_place)
# result = df_NNG_place['Column1'] + " " + df_NNG_place['Column2']
# print(result)

