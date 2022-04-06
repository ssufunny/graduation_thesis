import time
import pandas as pd
from konlpy.tag import Okt, Komoran, Mecab, Hannanum, Kkma


def get_tokenizer(tokenizer_name):
    global tokenizer
    if tokenizer_name == "komoran":
        tokenizer = Komoran()
    elif tokenizer_name == "okt":
        tokenizer = Okt()
    elif tokenizer_name == "mecab":
        tokenizer = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")
    elif tokenizer_name == "hannanum":
        tokenizer = Hannanum()
    elif tokenizer_name == "kkma":
        tokenizer = Kkma()
    else:
        tokenizer = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")
    return tokenizer


time_list = []
tokenizer_list = ["komoran", "okt", "mecab", "hannanum", "kkma"]
for i in tokenizer_list:
    start = time.time()
    tokenizer = get_tokenizer(i)
    f = open("C://graduation_thesis//graduation_thesis//test.txt", 'r', encoding='utf-8')
    text = f.read()
    tokenizer.morphs(text)
    # tokenizer.morphs("""한국어 자연어 처리 분야에 정말 괜찮은 책이 나왔다 출간되자 마자 읽어 보고 저자의 내공에 참 놀랐다 이렇게 좋은 품질의 도서가 더 많이 나와야 한다고 생각하는
    # 입장에서 저자에게 고마울 따름이다 하지만 네이버 책정보에도 YES24에도 이제까지 연결된 리뷰가 하나도 없다는 점이 좀 의아했다 네이버 블로그 리뷰는 좀 있음에도 그 이유는 아마도 책 제목 때문이 아닐까
    # 싶었다 아무래도 입문자 분들이 많이 봐야 할텐데 인공지능이나 딥러닝 같은 키워드가 아닌 한국어 임베딩이라고 제목이 달려있으니 뭔가 다른 기술이거나 아니면 매우 작은 범위의 기술로 착각할 수 있기 때문이다
    # 임베딩은 자연어 처리 뿐만 아니라 컴퓨터 비전 음성에서도 매우 중요한 키워드가 됐다 나 같은 경우 딥러닝 공부 초창기에 GAN에서 임베딩이라는 개념을 처음 접하게 되었는데 이걸 이해하려고 고생했던 기억이
    # 있다 딥러닝을 공부하면 할 수록 임베딩이라는 용어는 여러 개념을 관통하는 너무나 중요한 용어다. 이 책은 최신 자연어 처리 기술을 포함하고 있으며 이를 한국어에 맞게 적용할 수 있도록 일목요연하게 설명한
    # 책이다 특히 저자의 언어로 이러한 기술들을 설명한 점이 가장 중요하다 최근 자연어 처리 기술이 BERT를 통해 퀀텀 점프를 하였고 XLNet과 같은 후속 연구가 빠르게 진행되면서 급속하게 발전하고 있다
    # 저자는 BERT까지만 다루었는데 XLNet 같은 경우 직접 실험해보니 BERT보다 성능이 부족하다 판단하여 제외했다는 언급이 있다 이러한 부분이 책의 신뢰성을 더 높인다고 생각한다 직접 실험해보고
    # 고민해보고 이해한 흔적이 저자만의 언어로 설명되면 독자는 더 많은 통찰을 얻을 수 있다 데이터를 다루는 부분부터 소스코드도 괜찮고 그림 설명도 훌륭하다 다만 코드를 마이크로하게 설명하는 부분은 부족하여
    # 입문자 분들에겐 힘들수도 있지만 그래도 중요한 부분은 모두 언급했기 때문에 나쁘지 않다고 생각한다 한국어 용어도 내 입장에서는 매우 마음에 들었다 영어 발음 그대로 한국어로 쓰는 것을 싫어하시는 분들도
    # 계시겠지만 결국 최신 기술은 영어 논문을 읽어야 하기 때문에 어설프게 한국어로 번역된 용어 보다 훨씬 낫다고 생각한다 처음 나오는 전문용어 옆에는 영어로 표시하여 헷갈리지 않도록 충분히 배려했다 제발
    # 다른 번역서도 이 책을 참고하여 어설프게 한국어로 번역하지 않았으면 하는 바람이다 자연어 처리의 딥러닝 기술을 매우 잘 설명한 좋은 책이다 아직 리뷰가 하나도 없지만 더 많은 리뷰도 달리고 더 잘 팔려서
    # 최신 기술을 담은 2판이 나오길 희망한다""")
    time_required = time.time() - start
    tokenizer_and_time = i, time_required
    time_list.append(tokenizer_and_time)
print(time_list)
# 소요시간측정 = pd.DataFrame(time_list, columns=['토크나이저', '토큰화 소요시간'])
