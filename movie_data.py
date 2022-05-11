import pandas as pd
import openpyxl
import re

# filename = 'C://Users//jisu//Documents//한국외대//2022 - 1//정보통신종합설계//Data//movie_list.xlsx'
filename = 'C://graduation_thesis//movie_list.xlsx'
with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
    file_data = f.readlines()
file_data

movie_list = pd.read_excel(filename, engine="openpyxl")

for i in range(len(movie_list)):
    movie_name = movie_list.iloc[i, 1]
    if type(movie_name) == int:     # int 타입 예외
        result = str(movie_name)
        TF = '*'
    else:
        result = movie_name.replace(" ", "")    # 공백 제거
        last = movie_name[-1]
        # 한글 유무 판단
        name = re.search("[가-힣]+", last)
        # 받침 유무 판단
        if name:
            k = name.group()[-1]
            if ((ord(last)) - 44032) % 28 > 0:  # 받침 있음
                TF = 'T'
            else:
                TF = 'F'
        else:
            TF = '*'
    print(movie_name, result, TF)
    # mecab 사용자 사전에 추가
    file_data.append(result + ',,,,NNP,제목,' + TF + ',' + result + ',*,*,*,*\n')
    with open("C:/mecab/user-dic/nnp.csv", 'w', encoding='utf-8') as f:
        for line in file_data:
            f.write(line)