import copyreg
import re
import numpy as np
from konlpy.tag import Mecab
import MeCab
from collections import Counter

# mecab 위치 불러오기
mecab = Mecab(dicpath="C://mecab//mecab-ko-dic")
# text 파일 불러오기
# text 파일 위치(노트북)
# f = open("C://Users//jisu//Desktop//본문수집.txt", 'r', encoding='utf-8')
# text 파일 위치(컴퓨터)
f = open("C://graduation_thesis//graduation_thesis//test.txt", 'r', encoding='utf-8')
text_file = f.read()
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
w = []
for i in tagging:
    tag, category, TF, read, word_type, first_tag, last_tag, exp = i.split(',')
    num += 1
    if (category == '지명') or (category == '장소'):
        w.append(word[num])
        count = Counter(w)
tag_count = []
tags = []

for n, c in count.most_common(100):
    dics = {'tag': n, 'count': c}
    if len(dics['tag']) >= 2 and len(tags) <= 49:
        tag_count.append(dics)
        tags.append(dics['tag'])
for tag in tag_count:
    print(" {:<14}".format(tag['tag']), end='\t')
    print("{}".format(tag['count']))

