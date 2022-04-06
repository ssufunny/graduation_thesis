from konlpy.tag import Mecab
from collections import Counter

# mecab 위치 불러오기
mecab = Mecab(dicpath="C://mecab//mecab-ko-dic")
# text 파일 불러오기
f = open("C://Users//jisu//Desktop//본문수집.txt", 'r', encoding='utf-8')
text = f.read()

# 명사 추출
noun = mecab.nouns(text)
count = Counter(noun)

# 가장 많은 명사 100개 출력
noun_list = count.most_common(100)
for v in noun_list:
    print(v)