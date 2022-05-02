from konlpy.tag import Kkma, Okt, Mecab
import MeCab

kkma=Kkma()
okt=Okt()
mecab= Mecab(dicpath="C://mecab//mecab-ko-dic")
text = "여기는 서울특별시 동두천시 염치읍 삽교읍 모현읍 에버랜드 호미곶 롯데월드 롯데호텔 호텔 서점 창덕궁 백수읍 서울시 부산광역시 부산시 분당구 관악구 신림동 서현동 울진군 다도면 용두암 주상절리 오션월드 제이든가든 구글 대우 미스터 션샤인 만휴정 호텔 델루나 망상해수욕장 이태원 클라쓰 촬영지인 강원도 강릉시 영진해변입니다."

# print("Kkma 형태소 분석기")
# print(kkma.pos(text))
# print("Okt 형태소 분석기")
# print(okt.pos(text))
print("Mecab 형태소 분석기")
print(mecab.pos(text))
m = MeCab.Tagger()
print(m.parse(text))