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
f = open("C://graduation_thesis//graduation_thesis//myfile.txt", 'r', encoding='utf-8')
text_file = f.read()

# MeCab 이용
m = MeCab.Tagger()
print("MeCab 이용")
# parse 함수 사용(형태소 분석 & 품사 매칭)
texts = m.parse(text_file)
print(texts)