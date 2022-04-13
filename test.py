from konlpy.tag import Kkma, Okt, Mecab

kkma=Kkma()
okt=Okt()
mecab= Mecab(dicpath="C://mecab//mecab-ko-dic")
text = "여기는 도깨비 촬영지인 강원도 강릉시 영진 해변입니다."

print("Kkma 형태소 분석기")
print(kkma.pos(text))
print("Okt 형태소 분석기")
print(okt.pos(text))
print("Mecab 형태소 분석기")
print(mecab.pos(text))