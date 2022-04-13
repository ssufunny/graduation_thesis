from konlpy.tag import Mecab
import MeCab

# mecab 위치 불러오기
mecab = Mecab(dicpath="C://mecab//mecab-ko-dic")
# text 파일 불러오기
# text 파일 위치(노트북)
# f = open("C://Users//jisu//Desktop//본문수집.txt", 'r', encoding='utf-8')
# text 파일 위치(컴퓨터)
f = open("C://graduation_thesis//graduation_thesis//test.txt", 'r', encoding='utf-8')
text = f.read()

# MeCab 이용
m = MeCab.Tagger()
print("MeCab 이용")
# parse 함수 사용(형태소 분석 & 품사 매칭)
print(m.parse(text))

# Mecab 이용
print("Mecab 이용")
# pos 함수 사용(형태소 분석 & 품사 매칭)
print(mecab.pos(text))


# # 명사 추출
# noun = mecab.nouns(text)
# count = Counter(noun)
#
# # 가장 많은 명사 100개 출력
# noun_list = count.most_common(100)
# for v in noun_list:
#     print(v)
