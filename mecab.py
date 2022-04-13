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
# 생성된 배열 길이
words_len = len(words)  # 8328

tagging = []
word = []

# 단어와 품사 태깅 부분으로 배열 따로 지정
for i in range(0, words_len - 1):   # 배열 길이만큼 반복
    if i % 2 == 1:  # 품사 태깅
        tagging.append(words[i])
    else:   # 단어
        if words[i] != "EOS":   # "EOS" 제외한 단어만
            word.append(words[i])

# 생성된 배열 문자열로 합치기
tagging_join = ",".join(tagging)
# , 마다 split
tagging_split = re.split('[,]', tagging_join)
# 리스트 -> 배열
tagging_split_arr = np.array(tagging_split)
text = word + tagging_split
text_arr = np.array(text)
plz = []

for number in range(0, len(tagging_split_arr) - 1):
    if number % 8 == 1:
        plz.append(tagging_split[number])
plz_arr = np.array(plz)
word_arr = np.array(word)
# for ss in range(0, len(word) - 1):
#     print(ss, word_arr[ss], plz_arr[ss])
#     # print(number)

print(len(tagging_split))
word_arr = np.array(word)

result = []
result = [[str(1000)]*2 for i in range(len(tagging))]
result_arr = np.array(result)

for n in range(0, len(word) - 1):
    result_arr[n][0] = word_arr[n]
    result_arr[n][1] = plz_arr[n]
for sss in range(0, len(word) - 1):
    print(result_arr[sss])


#
# print(text)
# # print(tagging)
print(len(tagging)) # 4163
# print(len(word))    # 4163
# print(len(tagging_split))   # 33304
# print(len(text))    # 37467
# word_tagging = []
# print(word_split)
# print(tagging_split)
# text =
#
# for i in texts:
#     for j in range(7):
#         texts[i][j] =
# print(texts[0])


# # Mecab 이용
# print("Mecab 이용")
# # pos 함수 사용(형태소 분석 & 품사 매칭)
# print(mecab.pos(text_file))


# # 명사 추출
# noun = mecab.nouns(text)
# count = Counter(noun)
#
# # 가장 많은 명사 100개 출력
# noun_list = count.most_common(100)
# for v in noun_list:
#     print(v)
