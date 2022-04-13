import copyreg
import re

import numpy as np
from konlpy.tag import Mecab
import MeCab

# mecab 위치 불러오기
mecab = Mecab(dicpath="C://mecab//mecab-ko-dic")
# text 파일 불러오기
# text 파일 위치(노트북)
# f = open("C://Users//jisu//Desktop//본문수집.txt", 'r', encoding='utf-8')
# text 파일 위치(컴퓨터)
f = open("C://graduation_thesis//graduation_thesis//test.txt", 'r', encoding='utf-8')
text_file = f.read()

# MeCab 이용
m = MeCab.Tagger()
print("MeCab 이용")
# parse 함수 사용(형태소 분석 & 품사 매칭)
texts = m.parse(text_file)
# 띄어쓰기, 줄바꿈마다 split
words = re.split('[\t\n]', texts)

tagging = []
word = []
plz = []
result = []

# 단어와 품사 태깅 부분으로 배열 따로 지정
for i in range(0, len(words) - 1):   # 배열 길이만큼 반복
    if i % 2 == 1:  # 품사 태깅
        tagging.append(words[i])
    else:   # 단어
        if words[i] != "EOS":   # "EOS" 제외한 단어만
            word.append(words[i])

# 생성된 배열 문자열로 합치기
tagging_join = ",".join(tagging)
# , 마다 split
tagging_split = re.split('[,]', tagging_join)

# 지명 정보 부분만 추출
for number in range(0, len(tagging_split) - 1):
    if number % 8 == 1:
        plz.append(tagging_split[number])
# 결과 배열
result = [[str(1000)]*2 for i in range(len(tagging))]

# 결과 배열에 값 넣어주기
for n in range(0, len(word) - 1):
    result[n][0] = word[n]
    result[n][1] = plz[n]
# 단어별 출력
for m in range(0, len(word) - 1):
    print(result[m])