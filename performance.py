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
    time_required = time.time() - start
    tokenizer_and_time = i, time_required
    time_list.append(tokenizer_and_time)
print(time_list)
# 소요시간측정 = pd.DataFrame(time_list, columns=['토크나이저', '토큰화 소요시간'])
